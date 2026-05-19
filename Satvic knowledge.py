"""
HUMORIX — Satvic Lifestyle Intelligence
Complete knowledge base extracted from the Satvic Food Book.
Integrated into Humorix's AI system for holistic health guidance.
"""

# ── Core Philosophy ────────────────────────────────────────────────────────
SATVIC_PHILOSOPHY = """
SATVIC FOOD PHILOSOPHY (from Bhagavad Gita, Chapter 17):
- SATVIC (Mode of Goodness): Purity, happiness, compassion, bliss, self-control, fearlessness
- RAJASIK (Mode of Passion): Arrogance, restlessness, anxiety, anger, uncontrollable desires
- TAMASIK (Mode of Ignorance): Laziness, depression, lethargy, ignorance, illusion

THE 4 SATVIC FOOD PRINCIPLES (LWPW):
1. LIVING — Food straight from farm to kitchen. No packaged, tinned, bottled, or canned items.
2. WHOLESOME — Unprocessed, unrefined. Whole grains, dates, unpolished rice.
3. PLANT-BASED — From plants and trees, not animals. No meat, fish, eggs, or dairy.
4. WATER-RICH — High water content foods: fruits, vegetables, leafy greens dominate the diet.
"""

# ── 9 Satvic Food Laws ────────────────────────────────────────────────────
NINE_LAWS = [
    {
        "law": 1,
        "title": "No Dead Foods",
        "avoid": "Packaged, bottled, tinned, canned foods — chips, namkeens, snacks, sauces, dressings",
        "eat": "Living foods: fresh fruits, vegetables, grains, nuts, seeds straight from farm to kitchen"
    },
    {
        "law": 2,
        "title": "No Refined Foods",
        "avoid": "White sugar, white flour, white rice, refined oil",
        "eat": "Natural sweeteners (dates, jaggery), millets or whole wheat, brown/red rice, whole fats or cold-pressed oils"
    },
    {
        "law": 3,
        "title": "No Animal-Based Foods",
        "avoid": "Meat, fish, eggs, animal milk, cheese, butter, ghee, paneer",
        "eat": "Fresh homemade coconut milk, almond milk, cashew cheese, nut butter"
    },
    {
        "law": 4,
        "title": "Eat Less Grain, More Veggies",
        "avoid": "High percentage of grains and legumes in healing phase",
        "eat": "At least 2x more vegetables than grains or pulses"
    },
    {
        "law": 5,
        "title": "Eat Seasonal and Local",
        "avoid": "Imported fruits/vegetables, exotic ingredients not local to India (blueberries, kale, macadamia)",
        "eat": "Seasonal, regional foods that are cheaper and more aligned with your body"
    },
    {
        "law": 6,
        "title": "Always Soak Nuts",
        "avoid": "Unsoaked nuts — they contain enzyme inhibitors making them hard to digest",
        "eat": "Nuts soaked 6-8 hours before use — soaking activates them and increases digestibility"
    },
    {
        "law": 7,
        "title": "Use Mild Spices Only",
        "avoid": "Store-bought garam masala, red chili powder, excessive asafoetida (heeng)",
        "eat": "Fresh green chili, black pepper, fresh herbs: curry leaves, coriander, basil, lemongrass, oregano, rosemary, thyme"
    },
    {
        "law": 8,
        "title": "Minimal Cooking",
        "avoid": "High temperature for long duration, frying, over-cooking, pressure cooker for all vegetables",
        "eat": "Minimally cook for shortest duration possible at low or medium temperatures"
    },
    {
        "law": 9,
        "title": "No Stimulants",
        "avoid": "Tea, coffee, onions, garlic",
        "eat": "Herbal teas (lemongrass, tulsi, rose), coconut water"
    }
]

# ── 6 Laws of Mindful Eating ───────────────────────────────────────────────
MINDFUL_EATING_LAWS = [
    "Eat only when you feel genuine hunger — not out of boredom or habit",
    "Eat only till you're 3/4 full — leave space for digestive juices to mix",
    "Always eat in a relaxed, calm state — never when anxious, angry, or rushed",
    "Give your body 15 minutes rest after a heavy meal — don't resume work immediately",
    "Chew thoroughly — each mouthful well-mixed with saliva aids digestion",
    "Express gratitude before meals — acknowledge the journey food has made to reach you"
]

# ── Food Combining Laws ────────────────────────────────────────────────────
FOOD_COMBINING = {
    "rule_1": "In healing phase: only ONE grain or legume per meal (no rice + chapati, no rice + dal)",
    "rule_2": "Mix grains/legumes with 2x more vegetables",
    "rule_3": "Never mix fruits and cooked food in the same meal",
    "rule_4": "Never mix sweet fruits (mango, banana) with citric fruits (orange, lemon, pineapple)",
    "rule_5": "Don't drink water while eating — wait 1 hour before or 2 hours after",
    "rule_6": "Don't mix too many dishes — keep meals simple (2-3 types of food)"
}

# ── Fasting Window ─────────────────────────────────────────────────────────
FASTING = "Maintain 14-16 hours fasting window between dinner and breakfast daily for healing and repair"

# ── MEAL PLANS ─────────────────────────────────────────────────────────────

MEAL_PLANS = {

    "healing": {
        "name": "Healing Plan",
        "recommended_for": [
            "Thyroid imbalance", "Type 2 diabetes", "Menstrual disorders",
            "Digestive disorders", "Cardiovascular disease", "Respiratory disorders",
            "Excess weight", "Acne / skin problems", "Fatty liver",
            "Lethargy", "Migraines", "PCOD"
        ],
        "duration": "Maximum 3 months. Then switch to Lifestyle or Active plan.",
        "warning_signs_to_switch_early": [
            "Increased hair fall",
            "Excessive weakness or low energy sustained over time",
            "Rapid weight loss (more than 5-8 kg/month with muscle loss)",
            "Weight falling below desired weight"
        ],
        "schedule": {
            "pre_breakfast": {
                "time": "8:00 AM",
                "label": "Detox Juice",
                "options": [
                    "Ash Gourd Juice (safed petha) — 400 ml",
                    "Coconut Water — 400 ml (fresh only, never packaged)",
                    "Glowing Green Juice (cucumber, spinach, mint, apple, ginger, lemon)",
                    "ABC Juice (Apple, Beetroot, Carrot, Ginger)",
                    "Clean Carrot Juice (carrot, papaya, orange, ginger) — winter",
                    "Tomato Bathua Juice — winter"
                ],
                "note": "Ensure 1.5 to 2 hours gap between juice and breakfast"
            },
            "breakfast": {
                "time": "10:00 AM",
                "label": "Fruit-Based Breakfast",
                "options": [
                    "One single seasonal fruit (mono-eating — easiest to digest)",
                    "2+ seasonal fruits (avoid mixing sweet & citric)",
                    "Blush Smoothie Bowl (frozen banana, pear/apple, beetroot)",
                    "Green Smoothie Bowl (frozen banana, spinach, coconut, dates, cinnamon)",
                    "Banana Date Shake (banana, dates, coconut milk, cinnamon)",
                    "Marigold Smoothie (papaya, banana, dates, saffron, coconut milk)",
                    "Pure Satvic Salad (cucumber, carrot, tomato, capsicum, coconut, coriander, optional sprouts)",
                    "Clear Soup (lemongrass, seasonal veggies) — winter option"
                ],
                "notes": [
                    "Smoothies max 2-3 times/week — don't over-sweeten",
                    "Avoid poha, upma, packaged cereals during healing",
                    "Diabetics: choose guava, papaya, pear, apple — avoid mango, banana, chikoo; no smoothies"
                ]
            },
            "lunch": {
                "time": "1:00 PM",
                "label": "Grain Meal (principal meal of the day)",
                "options": [
                    "Satvic Roti (50% whole wheat flour + 50% seasonal vegetable like cucumber, beetroot, spinach, carrot)",
                    "Millet Roti (jowar or ragi flour with beetroot purée)",
                    "Satvic Sabzi (1-2 seasonal vegetables steamed in clay pot with tomato-coconut gravy)",
                    "Satvic Khichadi (1 cup brown rice + 4-5 cups vegetables)",
                    "Satvic Daliya (1:3 ratio — broken wheat to vegetables)",
                    "Millet Upma (barnyard/proso/foxtail millet + green beans, carrot, peas)",
                    "Spinach Cheela (50% split moong dal + 50% spinach)",
                    "Moong Bowl (soaked moong, fenugreek, fruits, seeds — fully raw)",
                    "Coco Quinoa Bowl (quinoa + cauliflower, potato, peas, coconut milk, thyme)",
                    "Golden Lentil Bowl (sprouted moong + vegetables + sesame tomato gravy)",
                    "Barley Bowl (barley + pumpkin, beetroot, mint tahini dressing)"
                ],
                "rules": [
                    "Only ONE grain or legume per meal",
                    "2-3x more vegetables than grains",
                    "Digestive fire is highest at noon — make this the main meal",
                    "Swap lunch and dinner freely based on your schedule"
                ],
                "chutneys": ["Green Chutney (coriander, mint, green chili, lemon, cumin)",
                             "Date Chutney", "Coconut Chutney"]
            },
            "mid_meal": {
                "time": "4:00 PM",
                "label": "Optional Mid-Meal",
                "options": [
                    "Fresh juice (any from pre-breakfast options)",
                    "Herbal Tea (lemongrass, cinnamon, cardamom, ginger, jaggery)",
                    "6-8 soaked nuts (almonds, peanuts, walnuts)",
                    "Fresh coconut kernel slices",
                    "Fresh coconut water"
                ],
                "note": "Skip if not hungry — don't snack mindlessly"
            },
            "dinner": {
                "time": "7:00 PM",
                "label": "Veggie Meal (NO grains in healing phase)",
                "salad_options": [
                    "Carrot Raisin Salad (grated carrot, sprouts, cashews, raisins, tahini dressing)",
                    "Cheesy Salad (broccoli, baby corn, bell peppers with cashew cheese)",
                    "Thai Papaya Salad (raw papaya, carrot, mango, tomato, peanut dressing)",
                    "Zesty Beet Salad (beetroot, lettuce, orange, coconut, Middle Eastern dressing)",
                    "Veggie Pasta Salad (bottle gourd strips, bell pepper, carrot in cashew sauce)",
                    "Sweet Potato Salad (sweet potato, lettuce, broccoli, tomato salsa)"
                ],
                "soup_options": [
                    "Pumpkin Soup (red pumpkin, coconut milk, thyme, rosemary)",
                    "Papaya Corn Soup (green papaya, lemongrass, coconut milk)",
                    "Spinach Soup (spinach, potato/singhara, coconut milk)",
                    "Pea Carrot Soup (fresh peas, carrot, potato, lemongrass)",
                    "Broccoli Potato Soup (broccoli, potato, ginger, coconut milk)",
                    "Tomato Soup (tomatoes, bottle gourd, carrot, herbs)",
                    "Carrot Cumin Soup (carrot, cauliflower, cumin, coconut milk)"
                ],
                "side_dish": ["Roasted Veggies (carrot, beans, zucchini, corn, bell pepper)",
                              "Vegetable Tikki (bottle gourd, cauliflower, peas, flaxseed)"],
                "rules": [
                    "No grains, rice, roti, millets, lentils or legumes in healing dinner",
                    "Can combine salad + soup",
                    "Underweight: add a small portion of grain or legume"
                ]
            }
        },
        "diabetic_adaptations": [
            "Choose low-sugar fruits: guava, papaya, pear, apple — avoid mango, chikoo, banana",
            "No smoothies — can spike blood sugar",
            "Best breakfast: Pure Satvic Salad"
        ],
        "underweight_adaptations": [
            "Add nut milk (soaked almonds/cashews/walnuts blended with water + dates) to fruit breakfast",
            "Add one grain/legume portion to veggie dinner",
            "Include 2-3 tablespoons cold-pressed oil unheated in meals",
            "Maintain protein: moong dal, chickpeas, kidney beans, green peas, nuts, seeds"
        ]
    },

    "lifestyle": {
        "name": "Lifestyle Plan",
        "recommended_for": [
            "Those who tend to gain weight easily",
            "Sedentary lifestyle (sitting most of the day, exercising max 1 hour)"
        ],
        "schedule": {
            "pre_breakfast": {"time": "8:00 AM", "label": "Detox Juice",
                              "options": ["Ash gourd juice", "Coconut water", "Green juice", "ABC juice"]},
            "breakfast": {"time": "10:00 AM", "label": "Fruits + Soaked Nuts",
                          "options": ["Plain simple fruits + handful of soaked nuts",
                                      "Smoothie (2-3 times/week)"]},
            "lunch": {"time": "1:00 PM", "label": "Grain + Legume Meal with Lots of Veggies",
                      "note": "1 portion grain (millets, wheat, rice) + 1 portion legume (dal, chickpeas) + 2 portions vegetables"},
            "mid_meal": {"time": "4:00 PM", "label": "Optional",
                         "options": ["Coconut water", "Fruits", "Coconut kernel or 7-8 soaked nuts"]},
            "dinner": {"time": "7:00 PM", "label": "Salad or Soup + Optional Grain/Legume",
                       "note": "If salad/soup doesn't satiate, add a small bowl of legumes or lentils"}
        }
    },

    "active": {
        "name": "Active Plan",
        "recommended_for": [
            "Underweight or tendency to lose weight easily",
            "Highly active lifestyle (intense or long hours of physical activity daily)"
        ],
        "schedule": {
            "pre_breakfast": {"time": "8:00 AM", "label": "Detox Juice or Fruits",
                              "options": ["Ash gourd juice", "ABC Juice",
                                          "Fruits + handful of soaked nuts", "Smoothie"]},
            "breakfast": {"time": "10:00 AM", "label": "Legume or Grain-Based Dish",
                          "options": ["Moong sprout salad", "Spinach Cheela", "Millet Dosa"]},
            "lunch": {"time": "1:00 PM", "label": "Grain + Legume Meal with Lots of Veggies",
                      "note": "1 portion grain + 1 portion legume + 2 portions vegetables"},
            "mid_meal": {"time": "4:00 PM", "label": "Fruits or Nut-Based Snack",
                         "options": ["Fruits", "Any fruit with nut butter", "Smoothie with nuts"]},
            "dinner": {"time": "7:00 PM", "label": "Grain or Veggie Meal",
                       "options": ["Grain + legume meal with lots of veggies",
                                   "Sautéed veggies with grain/legume", "Soup", "Salad"]}
        }
    }
}

# ── Nutrition Guide ────────────────────────────────────────────────────────
NUTRITION = {
    "protein": {
        "requirement": "0.83g per kg body weight (WHO) for moderately active adults",
        "sources": {
            "Cooked chickpeas": "15g per cup",
            "Cooked lentils (masoor etc)": "18g per cup",
            "Sprouts (raw)": "7g per cup",
            "Green peas": "8g per cup",
            "Homemade tofu": "20g per cup",
            "Cooked kidney beans": "15g per cup",
            "Cooked lobia": "13g per cup",
            "Peanuts (handful)": "7g",
            "Peanut butter (2 tbsp)": "8g",
            "Cashew nuts (handful)": "5g",
            "Almonds (handful)": "6g",
            "Pumpkin seeds (handful)": "5g",
            "Chia seeds (1 cup)": "5g",
            "Sesame seeds (1 cup)": "5g",
            "Brown rice (1 cup)": "5g",
            "Wheat chapati (1)": "3g",
            "Cooked millets (1 cup)": "6g"
        },
        "note": "Healing plan intentionally keeps protein low for easier digestion and better healing. Switch to lifestyle/active plan after 3 months."
    },
    "calcium": {
        "note": "Plants provide calcium directly without going through the cow",
        "top_sources": {
            "Sesame seeds": "1283mg per 100g",
            "Poppy seeds": "1438mg per 100g",
            "Finger millet (ragi)": "364mg per 100g",
            "Whole horsegram (kulhi)": "269mg per 100g",
            "Drumstick leaves": "314mg per 100g",
            "Fenugreek leaves (methi)": "275mg per 100g",
            "Amaranth leaves (cholai)": "245mg per 100g",
            "Quinoa": "198mg per 100g"
        }
    },
    "vitamin_d": {
        "best_source": "15-20 minutes direct sunlight, 3-5 times per week",
        "note": "Get blood test done. Supplement if deficient. Maintain via regular sunbathing once normalized."
    },
    "vitamin_b12": {
        "note": "B12 is made by soil microorganisms. Modern farming depletes natural B12 sources.",
        "recommendation": "Get blood test done. Supplement under physician guidance if deficient. B12 is one of the few nutrients not available in sufficient quantities from food alone."
    }
}

# ── Sprouts Guide ─────────────────────────────────────────────────────────
SPROUTS = {
    "why": "Sprouts are 10-30x more nutritious than the full-grown vegetable. Most concentrated living food.",
    "how_to_grow": [
        "Rinse seeds, soak overnight in filtered water",
        "Drain and rinse in the morning",
        "Tie in a muslin cloth",
        "Place in bowl, cover, keep away from direct sunlight",
        "Rinse twice daily (morning and evening)",
        "Ready in 3-5 days depending on seed type"
    ],
    "varieties": {
        "Alfalfa": "5 days, 1 tbsp seeds = 1 cup sprouts",
        "Clover": "5 days, 1 tbsp = 1 cup",
        "Radish": "5 days, 2 tbsp = 1 cup",
        "Fenugreek": "3 days, 1 tbsp = 1.5 cups",
        "Moong": "3 days, 0.5 cup = 2 cups",
        "Green Lentils": "3 days, 0.5 cup = 2 cups",
        "Chickpeas": "3 days, 0.5 cup = 1.5 cups",
        "Black Chickpeas": "3 days, 0.5 cup = 1.5 cups"
    },
    "salad_ratio": "30% sprouts + 30% vegetables + 30% leafy greens + 10% toppings (coconut, nuts, seeds, dressing)"
}

# ── Nut Milks ──────────────────────────────────────────────────────────────
NUT_MILKS = {
    "coconut_milk": "1 cup fresh coconut + 2 cups water, blend, strain. Use immediately or refrigerate max 1-2 days.",
    "almond_milk": "1/4 cup soaked almonds (6 hours) + 1 cup water, blend, strain.",
    "sesame_milk": "1/4 cup soaked sesame seeds (6 hours) + 1 cup water, blend, strain.",
    "rules": [
        "Always make fresh at home — never buy packaged nut milks",
        "Soak nuts minimum 6 hours before blending",
        "Discard soaking water",
        "Do NOT cook coconut milk directly on flame — always add after switching off stove"
    ]
}

# ── Winter Variations ──────────────────────────────────────────────────────
WINTER_VARIATIONS = {
    "Morning juice": "Replace ash gourd with Carrot juice, ABC juice, or Bathua-Tomato juice",
    "Breakfast": "Replace fruits/smoothies with simple homemade vegetable soups",
    "Mid-meal": "Replace coconut water/juices with warm herbal teas"
}

# ── Special Occasions ──────────────────────────────────────────────────────
SPECIAL_OCCASIONS = {
    "drinks": ["Coconut Chaas (mint, lemon, cumin, coconut milk, water)",
               "Thandai (almonds, fennel, poppy seeds, dates, coconut milk, saffron, cardamom)",
               "No-Coffee Cold-Coffee (roasted date seeds or chickpeas as coffee substitute)"],
    "breakfast": ["Chocolate Smoothie Bowl (frozen banana, dates, coconut milk, cacao)",
                  "Sabja Pudding (sabja/chia seeds in coconut milk with fruits)"],
    "main_course": ["Thai Curry with Brown Rice (homemade Thai paste, seasonal vegetables, coconut milk)"],
    "desserts": ["Satvic Kheer (kodo millet, almond milk, jaggery, saffron)",
                 "Satvic Gajar Halwa (red carrots, jaggery, coconut milk, cardamom)",
                 "Kulfi (cashews, coconut malai, dates, saffron, cardamom)",
                 "Peanut Butter Ice Cream (frozen bananas, homemade peanut butter, dates)",
                 "Satvic Ladoo (dry coconut butter, almond butter, jaggery)",
                 "Lemon Cheesecake (cashew base, lime gel, ginger crumble — no dairy, no sugar)"]
}

# ── Skin Care ──────────────────────────────────────────────────────────────
SKIN_CARE = {
    "rose_cleanser": {
        "ingredients": "1 cup oats + 1 tablespoon besan (gram flour) + 1/4 cup dry rose petals",
        "method": "Blend into powder. Mix 1 tbsp with 1.5 tsp water to form paste. Apply to face/body in circular motion 3-5 mins. Rinse.",
        "suitable_for": "All skin types — dry, oily, sensitive",
        "storage": "Airtight container up to 2 weeks. Keep dry."
    }
}

# ── Satvic System Prompt for Humorix ──────────────────────────────────────
SATVIC_SYSTEM_CONTEXT = """
SATVIC LIFESTYLE KNOWLEDGE (Integrated from Satvic Food Book by Subah Saraf):

You have deep knowledge of the Satvic lifestyle — a holistic Indian health philosophy rooted 
in Bhagavad Gita principles. When users ask about food, health, diet, or wellness, 
you naturally draw from this wisdom.

KEY PRINCIPLES:
- Food is either Satvic (pure, living, plant-based, water-rich), Rajasik (stimulating, spicy), or Tamasik (stale, dead)
- The 4 Food Principles: Living, Wholesome, Plant-Based, Water-Rich (LWPW)
- 9 Food Laws: no dead foods, no refined foods, no animal products, less grain, seasonal/local, soak nuts, mild spices, minimal cooking, no stimulants
- 6 Mindful Eating Laws: eat when hungry, stop at 3/4 full, eat relaxed, rest after meals, chew thoroughly, express gratitude

THREE MEAL PLANS:
1. HEALING PLAN — For reversing chronic disease (max 3 months). Morning juice → fruit breakfast → grain lunch → optional mid-meal → veggie-only dinner. No grains at dinner.
2. LIFESTYLE PLAN — For those with sedentary lifestyle or tendency to gain weight. Similar structure but includes legumes at lunch and optional grain/legume at dinner.  
3. ACTIVE PLAN — For underweight or highly active people. Grain+legume breakfast, grain+legume lunch, grain or veggie dinner.

HEALING PLAN DAILY SCHEDULE:
- 8:00 AM: Detox juice (ash gourd/coconut water/green juice/ABC juice)
- 10:00 AM: Fruit meal or Satvic salad
- 1:00 PM: Grain + vegetable meal (2-3x more veggies than grain)
- 4:00 PM: Optional — herbal tea, soaked nuts, coconut water
- 7:00 PM: Vegetable dinner — salad OR soup (no grains)
- Fasting window: 14-16 hours between dinner and morning juice

IMPORTANT ALWAYS:
- Recommend professional consultation for serious health conditions
- The Satvic approach supports, not replaces, medical care
- Adapt advice based on the user's specific health situation (diabetic, underweight, etc.)
"""

def get_meal_plan(plan_type: str) -> dict:
    """Get a specific meal plan by type: healing, lifestyle, or active."""
    return MEAL_PLANS.get(plan_type.lower(), MEAL_PLANS["healing"])

def get_food_law(law_number: int) -> dict:
    """Get a specific food law by number (1-9)."""
    for law in NINE_LAWS:
        if law["law"] == law_number:
            return law
    return {}

def get_all_dinner_options() -> dict:
    """Get all dinner options from healing plan."""
    return MEAL_PLANS["healing"]["schedule"]["dinner"]

def get_breakfast_options() -> list:
    """Get all breakfast options from healing plan."""
    return MEAL_PLANS["healing"]["schedule"]["breakfast"]["options"]

def recommend_plan(condition: str) -> str:
    """Recommend a meal plan based on health condition."""
    condition_lower = condition.lower()
    healing_conditions = [
        "diabetes", "thyroid", "pcod", "pcos", "weight", "obesity",
        "acne", "skin", "digestive", "heart", "cholesterol", "fatty liver",
        "migraine", "respiratory", "menstrual"
    ]
    active_conditions = ["underweight", "thin", "lose weight", "active", "athlete", "gym"]

    for c in healing_conditions:
        if c in condition_lower:
            return "healing"
    for c in active_conditions:
        if c in condition_lower:
            return "active"
    return "lifestyle"