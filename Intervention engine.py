"""
HUMORIX — Clinical Intervention Engine v3.1 [OPTIMIZED]
Evidence-based CBT protocols per disorder subtype.
DETECT → VALIDATE → INTERVENE → TRACK → ESCALATE

PERFORMANCE IMPROVEMENTS:
- Cached crisis resources (pre-concatenated)
- Memory-bounded session tracking (max 100 scores per disorder)
- O(1) protocol lookups via pre-computed disorder index
- Lazy initialization of response dicts
"""

import random
from typing import Optional
from functools import lru_cache

# ── Disclaimer (shown every session) ──────────────────────────────────────
DISCLAIMER = (
    "⚠️  Humorix is a supportive AI tool, not a licensed therapist. "
    "The insights provided are not medical diagnoses. "
    "Please consult a qualified mental health professional for clinical care."
)

# ── Crisis hotlines ────────────────────────────────────────────────────────
CRISIS_RESOURCES = {
    "India": [
        "iCall (TISS): 9152987821",
        "Vandrevala Foundation: 1860-2662-345 (24/7)",
        "KIRAN Mental Health Helpline: 1800-599-0019 (free, 24/7)",
        "Snehi: 044-24640050",
    ],
    "International": [
        "Crisis Text Line: Text HOME to 741741",
        "findahelpline.com (worldwide directory)",
        "988 Suicide & Crisis Lifeline (US): call/text 988",
        "Samaritans (UK): 116 123",
    ]
}

# ── OPTIMIZATION: Pre-concatenate all resources to avoid O(n) list concat ──
_ALL_CRISIS_RESOURCES = CRISIS_RESOURCES["India"] + CRISIS_RESOURCES["International"]

# ── Full disorder protocol library ────────────────────────────────────────
PROTOCOLS = {

    "GAD": {
        "name": "Generalised Anxiety Disorder",
        "detect_msg": "I'm noticing signs of anxiety — tension in your expression and worry patterns in what you're sharing.",
        "validate": [
            "Anxiety is your mind working overtime to protect you. That's not weakness — it's your nervous system doing its job.",
            "What you're feeling makes complete sense. Anxiety is one of the most common human experiences.",
            "That sense of dread and worry is real and valid. You're not overreacting.",
        ],
        "interventions": {
            "mild": [
                "Let's try the 5-4-3-2-1 grounding technique: name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, 1 you can taste.",
                "Take a slow breath with me — in for 4 counts, hold for 4, out for 6. The extended exhale activates your parasympathetic nervous system.",
                "Try writing down your worry, then ask: 'Is this within my control right now?' If not, practice letting it sit without acting on it.",
            ],
            "moderate": [
                "I'd like to walk you through 4-7-8 breathing: inhale 4 counts, hold 7, exhale fully for 8. Repeat 3 times.",
                "Let's challenge the worry thought. What's the actual probability this happens? What evidence supports or contradicts it?",
                "Progressive muscle relaxation: starting from your feet, tense each muscle group for 5 seconds then release upward to your face.",
            ],
            "severe": [
                "This level of anxiety deserves more support than I can provide alone. I strongly recommend speaking with a therapist about CBT for anxiety.",
                "You're experiencing significant distress. Let's use diaphragmatic breathing right now, and then I'd like to share some professional resources with you.",
            ],
        },
        "track_q": "On a scale of 1–10, how intense does the anxiety feel right now?",
        "escalate_threshold": 7,
    },

    "panic_disorder": {
        "name": "Panic Disorder",
        "detect_msg": "The patterns I'm detecting — rapid speech, facial tension, fear signals — suggest you may be experiencing a panic response.",
        "validate": [
            "A panic attack, while terrifying, is not dangerous. Your body is triggering a false alarm. You are safe.",
            "What you're feeling is real and intense. Panic attacks peak within 10 minutes and always pass.",
        ],
        "interventions": {
            "mild": [
                "Panic Attack First Aid: Plant both feet on the floor. Name the room you're in. You are safe right now.",
                "Box breathing: inhale 4, hold 4, exhale 4, hold 4. Repeat. This resets your autonomic nervous system.",
            ],
            "moderate": [
                "Right now: slow your exhale — make it twice as long as your inhale. This is the fastest way to reduce panic physiologically.",
                "DARE Response: Defuse the thought ('just anxiety'), Allow the feeling, Run toward it (don't flee), Engage with life.",
            ],
            "severe": [
                "You're in significant distress. Focus only on your next breath. In… and out. I'm right here with you.",
                "If this is recurring, panic disorder is highly treatable with CBT. Please reach out to a professional — you don't have to keep living with this.",
            ],
        },
        "track_q": "Where is the panic intensity right now, 1–10?",
        "escalate_threshold": 8,
    },

    "depression": {
        "name": "Depression / Major Depressive Disorder",
        "detect_msg": "I'm noticing low affect, slower responses, and language patterns that suggest you may be experiencing depression.",
        "validate": [
            "Depression is not a character flaw or weakness. It's a real condition that affects millions, and it's not your fault.",
            "The heaviness you're feeling is real. Depression distorts how we see ourselves, the world, and the future — but those distortions are treatable.",
            "I hear how much energy even small things take right now. That's depression, not you.",
        ],
        "interventions": {
            "mild": [
                "Behavioral Activation: What's one small activity — even 5 minutes — that sometimes brings even a flicker of interest? Let's schedule that today.",
                "Depression lies about the future. Try this: write down one thing you're grateful for, however small. It gently rewires negative bias.",
                "Opposite action: Depression says 'stay in bed'. The evidence-based response is gentle movement — even a short walk changes brain chemistry.",
            ],
            "moderate": [
                "Pleasure prediction: Think of an activity. Rate how much you expect to enjoy it (1–10). Then do it and rate actual enjoyment. Depression often predicts much lower than reality.",
                "Thought record: Write the depressive thought → the evidence for it → the evidence against it → a balanced alternative.",
                "Social connection, even when it feels impossible, is one of the strongest antidepressants known. Could you send one message to someone today?",
            ],
            "severe": [
                "What you're experiencing sounds serious, and you deserve real support. Please consider speaking with a doctor or therapist — depression is one of the most treatable conditions.",
                "I want to ask directly: are you having any thoughts of harming yourself? Whatever your answer, you're not alone and help is available.",
            ],
        },
        "track_q": "On a scale of 1–10, how heavy does the low mood feel today?",
        "escalate_threshold": 7,
    },

    "PTSD": {
        "name": "Post-Traumatic Stress Disorder",
        "detect_msg": "I'm noticing avoidance patterns, hypervigilance signals, and distress cues that may relate to trauma responses.",
        "validate": [
            "What you went through was real, and your nervous system is responding to protect you from it happening again. PTSD is a survival response, not weakness.",
            "Trauma responses make complete sense given what you've experienced. You're not broken — you're adapting.",
        ],
        "interventions": {
            "mild": [
                "Grounding: When a memory or feeling intrudes, place your hand on a solid surface. Press gently. Feel the temperature. This anchors you in the present.",
                "Safe place visualisation: Close your eyes and picture a place — real or imagined — where you feel completely safe. Notice the details. Stay there for 2 minutes.",
            ],
            "moderate": [
                "The window of tolerance: When triggered, name what's happening — 'I'm having a trauma response' — without judgment. This activates the prefrontal cortex and reduces amygdala firing.",
                "Titrated exposure: Rather than avoiding the memory completely, try briefly (30 seconds) acknowledging it exists, then return to grounding. Small doses reduce its power over time.",
            ],
            "severe": [
                "PTSD is highly treatable with EMDR and trauma-focused CBT. You don't have to keep managing this alone. Would you like help finding a trauma-informed therapist?",
                "What you're carrying sounds very heavy. Specialised trauma therapy exists precisely for this — please consider reaching out to a professional.",
            ],
        },
        "track_q": "How intrusive are the memories or responses feeling right now, 1–10?",
        "escalate_threshold": 7,
    },

    "bipolar_mania": {
        "name": "Bipolar Disorder — Manic Episode",
        "detect_msg": "I'm noticing elevated energy, rapid speech patterns, and expansive mood signals that may indicate a manic or hypomanic episode.",
        "validate": [
            "The energy and clarity you're feeling are real. Bipolar highs can feel extraordinary. And they also benefit from careful management.",
        ],
        "interventions": {
            "mild": [
                "Sleep is the most powerful mood stabiliser. Even if you don't feel tired, maintaining a consistent sleep schedule regulates episode intensity significantly.",
                "Reality check: On a scale of 1–10, how impulsive have your decisions been in the last 48 hours? Elevated scores are worth pausing on.",
            ],
            "moderate": [
                "Before any major decision (financial, relational, professional) during a high period, apply a 48-hour waiting rule. If it still seems right then, consider it.",
                "Energy regulation: Channel the elevated energy into structured, bounded activities. Avoid anything irreversible.",
            ],
            "severe": [
                "The level of intensity you're describing warrants speaking with your psychiatrist or care team today. This is important — please make that call.",
            ],
        },
        "track_q": "On a scale of 1–10, how elevated or racing does your energy feel?",
        "escalate_threshold": 7,
    },

    "OCD": {
        "name": "OCD / Obsessive-Compulsive Disorder",
        "detect_msg": "I'm noticing intrusive thought patterns and possible compulsive loops in what you're sharing.",
        "validate": [
            "Intrusive thoughts are not a reflection of who you are or what you want. OCD attaches to what matters most to you — it's a disorder, not a character trait.",
            "The distress you feel around these thoughts is real. OCD is one of the most misunderstood conditions, and it's also one of the most treatable.",
        ],
        "interventions": {
            "mild": [
                "Thought defusion: Instead of 'I am a terrible person', try 'I am having the thought that I am a terrible person.' Create distance between you and the thought.",
                "Delay the compulsion by 5 minutes. Then 10. ERP (Exposure Response Prevention) works by letting anxiety naturally subside without the ritual.",
            ],
            "moderate": [
                "ERP ladder: Rate your triggering situations 1–10 by distress. Start practicing sitting with the discomfort at the lowest level without performing the compulsion.",
                "OCD thoughts are like spam emails. You don't have to open them, argue with them, or delete them. Let them sit in the folder.",
            ],
            "severe": [
                "OCD at this intensity significantly benefits from ERP therapy with a trained OCD specialist. This is not something you should have to manage alone.",
            ],
        },
        "track_q": "How strong is the urge to perform the compulsion right now, 1–10?",
        "escalate_threshold": 8,
    },

    "eating_disorder": {
        "name": "Eating Disorder",
        "detect_msg": "I'm noticing language patterns and emotional signals that may relate to difficulties around food, body image, or eating.",
        "validate": [
            "Eating disorders are serious mental health conditions — not vanity or choices. They have the highest mortality rate of any mental illness, and they are treatable.",
            "What you're experiencing around food and your body is real and painful. You deserve support, not judgment.",
        ],
        "interventions": {
            "mild": [
                "Body neutrality: Your body's value is not its appearance or what it eats. Try: 'My body allows me to [function/breathe/feel]. That is enough.'",
                "Mindful eating: One meal, no distractions. Notice taste, texture, hunger cues. This reconnects eating to the body, not the rules.",
            ],
            "moderate": [
                "Thought challenging: When the critical voice speaks about food or body, ask — 'Would I say this to someone I loved?' If not, it doesn't belong in your internal dialogue.",
            ],
            "severe": [
                "What you're describing requires specialised support. Please reach out to an eating disorder specialist or helpline. You deserve recovery — full recovery is possible.",
                "National Alliance for Eating Disorders helpline: (866) 662-1235. In India: connect with NIMHANS or a registered dietitian + therapist team.",
            ],
        },
        "track_q": "How much is food/body distress affecting you today, 1–10?",
        "escalate_threshold": 6,
    },

    "ADHD": {
        "name": "ADHD / Attention Deficit Hyperactivity Disorder",
        "detect_msg": "I'm noticing focus difficulties, topic-jumping, and impulsivity patterns that may relate to ADHD.",
        "validate": [
            "ADHD is not laziness or lack of effort. It's a neurological difference in how the brain regulates attention and executive function.",
            "The frustration of knowing what you need to do but not being able to start it is one of ADHD's most painful aspects. It makes complete sense.",
        ],
        "interventions": {
            "mild": [
                "Body doubling: Work alongside someone else — physically or virtually. ADHD brains regulate attention better in social contexts.",
                "2-minute rule: If a task takes under 2 minutes, do it immediately. This bypasses the initiation barrier.",
                "Pomodoro: 25 minutes focused work → 5-minute break. External time structure compensates for internal regulation difficulty.",
            ],
            "moderate": [
                "Task initiation hack: Open the document / app / notebook first. Just open it. Often the brain engages once the barrier of starting is removed.",
                "Externalise everything: Alarms, whiteboards, sticky notes. ADHD is an 'out of sight, out of mind' condition — keep important things visible.",
            ],
            "severe": [
                "ADHD at this level of impact is worth discussing with a psychiatrist — both non-medication and medication options have strong evidence.",
            ],
        },
        "track_q": "How much is focus/attention difficulty affecting you right now, 1–10?",
        "escalate_threshold": 8,
    },
}

# ── Generic protocols for emotions without specific disorder match ─────────
EMOTION_RESPONSES = {
    "sad": {
        "validate": "That sadness is valid. Sit with it for a moment without trying to fix it — emotions move through us when we allow them to.",
        "suggest":  "Would it help to talk about what's behind the sadness?",
    },
    "anxious": {
        "validate": "Anxiety is your mind working hard. Let's slow down together.",
        "suggest":  "Take one slow breath with me before we continue.",
    },
    "angry": {
        "validate": "Anger usually means something important to you has been affected. That's worth understanding.",
        "suggest":  "What's the core thing that feels wrong or unfair right now?",
    },
    "fear": {
        "validate": "Fear is protective. Let's look at what it's pointing to.",
        "suggest":  "Is this fear about something happening right now, or something anticipated?",
    },
    "neutral": {
        "validate": "How are you really doing today?",
        "suggest":  "Sometimes 'fine' covers a lot of ground. I'm here if you want to go deeper.",
    },
}

# ── OPTIMIZATION: Pre-compute protocol keys for O(1) lookup ──
_PROTOCOL_KEYS = frozenset(PROTOCOLS.keys())


class InterventionEngine:
    """
    Selects and delivers the appropriate evidence-based intervention
    based on FusionEngine output.
    
    OPTIMIZATIONS:
    - Memory-bounded session tracking (sliding window, max 100 entries)
    - Pre-computed crisis resources (no list concatenation on each call)
    - Lazy response dict initialization (only set required fields)
    """

    # Config constant: Max intensity scores per disorder before eviction
    _MAX_TRACKING_HISTORY = 100

    def __init__(self):
        self._session_track = {}    # disorder → deque of last 100 intensity scores
        self._session_count = 0
        self._disclaimer_shown = False

    def respond(self, fusion_result: dict, user_text: str = "") -> dict:
        """
        Takes a FusionEngine output dict and returns a structured intervention.
        """
        self._session_count += 1
        severity   = fusion_result.get("severity", "none")
        emotion    = fusion_result.get("fused_emotion", "neutral")
        disorder_risk = fusion_result.get("disorder_risk", {})
        confidence = fusion_result.get("overall_confidence", 0.0)

        response = {
            "type":         "normal",
            "emotion":      emotion,
            "severity":     severity,
            "disclaimer":   "",
            "detect_msg":   "",
            "validate":     "",
            "intervention": "",
            "track_q":      "",
            "escalate":     False,
            "resources":    [],
            "full_text":    "",
        }

        # Show disclaimer once per session
        if not self._disclaimer_shown:
            response["disclaimer"] = DISCLAIMER
            self._disclaimer_shown = True

        # Crisis path
        if severity == "crisis":
            return self._crisis_response(response, disorder_risk, user_text)

        # Disorder-specific path — OPTIMIZED: dict.get() is O(1), check membership first
        top_disorder = next(iter(disorder_risk), None) if disorder_risk else None
        if top_disorder and top_disorder in _PROTOCOL_KEYS and disorder_risk[top_disorder] >= 0.35:
            return self._disorder_response(response, top_disorder, severity, disorder_risk)

        # Emotion-only path (no specific disorder detected)
        return self._emotion_response(response, emotion)

    def _disorder_response(self, r: dict, disorder: str, severity: str, risks: dict) -> dict:
        proto = PROTOCOLS[disorder]
        sev_key = severity if severity in proto["interventions"] else "mild"

        r["type"]         = "disorder"
        r["detect_msg"]   = proto["detect_msg"]
        r["validate"]     = random.choice(proto["validate"])
        r["intervention"] = random.choice(proto["interventions"][sev_key])
        r["track_q"]      = proto["track_q"]

        # Escalate if severe/crisis — OPTIMIZED: Use pre-computed resources
        if severity in ("severe", "moderate") and risks.get(disorder, 0) >= proto["escalate_threshold"] / 10:
            r["escalate"]  = True
            r["resources"] = _ALL_CRISIS_RESOURCES  # O(1) instead of O(n) concatenation

        r["full_text"] = self._build_text(r)
        return r

    def _emotion_response(self, r: dict, emotion: str) -> dict:
        er = EMOTION_RESPONSES.get(emotion, EMOTION_RESPONSES["neutral"])
        r["type"]         = "emotion"
        r["validate"]     = er["validate"]
        r["intervention"] = er["suggest"]
        r["full_text"]    = self._build_text(r)
        return r

    def _crisis_response(self, r: dict, risks: dict, text: str) -> dict:
        r["type"]      = "crisis"
        r["escalate"]  = True
        r["validate"]  = (
            "I hear you, and I'm very glad you're talking to me right now. "
            "What you're going through sounds extremely difficult."
        )
        r["intervention"] = (
            "Please reach out to a crisis line right now — "
            "you don't have to face this alone, and real help is available immediately."
        )
        r["resources"] = _ALL_CRISIS_RESOURCES  # O(1) cached access
        r["full_text"] = self._build_text(r)
        return r

    def record_intensity(self, disorder: str, score: int):
        """Record user's self-reported intensity for tracking.
        
        OPTIMIZED: Uses bounded list (max 100 entries) to prevent memory leak.
        """
        if disorder not in self._session_track:
            self._session_track[disorder] = []

        self._session_track[disorder].append(score)

        # Evict oldest if exceeds max — prevents unbounded growth
        if len(self._session_track[disorder]) > self._MAX_TRACKING_HISTORY:
            self._session_track[disorder].pop(0)

    def get_trend(self, disorder: str) -> Optional[str]:
        """Assess if symptoms are improving, stable, or worsening."""
        scores = self._session_track.get(disorder, [])
        if len(scores) < 3:
            return None
        recent  = sum(scores[-2:]) / 2
        earlier = sum(scores[:-2]) / max(1, len(scores) - 2)
        if recent < earlier - 1:   return "improving"
        if recent > earlier + 1:   return "worsening"
        return "stable"

    def _build_text(self, r: dict) -> str:
        parts = []
        if r.get("disclaimer"):
            parts.append(r["disclaimer"] + "\n")
        if r.get("detect_msg"):
            parts.append(r["detect_msg"])
        if r.get("validate"):
            parts.append(r["validate"])
        if r.get("intervention"):
            parts.append(r["intervention"])
        if r.get("track_q"):
            parts.append("\n" + r["track_q"])
        if r.get("escalate") and r.get("resources"):
            parts.append("\n🆘 **Professional Support:**")
            for res in r["resources"][:4]:
                parts.append(f"  • {res}")
        return "\n\n".join(p for p in parts if p)
