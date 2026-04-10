from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# ==================== CHARACTER DATA (expand as needed) ====================
characters = {
    "elesis": {
        "name": "Elesis",
        "role": "Melee DPS / Tank",
        "image": "https://picsum.photos/id/1015/800/600",
        "description": "Leader of the Grand Chase. Excellent starter character with strong AoE and defense.",
        "leveling_tips": "Focus on story quests + Hero Dungeons. Equip Angel Ring at Lv20 for +50% EXP. Aim for Lv85 in 4-6 hours.",
        "job_path": "1st: Knight → 2nd: Spearman → 3rd: Sword Master → 4th: Savior",
        "skill_recommend": "Max Mega Slash & Flame Strike. Prioritize Crit and Attack Speed in skill tree.",
        "equipment": "Coordi sets for Crit Chance + Attack. Reinforce to +15, transcend gear for endgame.",
        "awakening": "Unlock after Lv85. Focus on 4th bar special skill and stat growth. Priority for main DPS.",
        "tips": "Great for beginners. Use in PvE and PvP. Build Hero Collection for account-wide bonuses."
    },
    "lire": {
        "name": "Lire",
        "role": "Ranged DPS",
        "image": "https://picsum.photos/id/1005/800/600",
        "description": "Elf archer with high mobility and burst damage.",
        "leveling_tips": "Fast clear speed in dungeons. Use Z-Charge skill spam for quick leveling.",
        "job_path": "1st: Archer → 2nd: Crossbow → 3rd: Sniper → 4th: Celestial",
        "skill_recommend": "Prioritize multi-shot skills and critical hits.",
        "equipment": "Focus on Attack and Critical Damage coordi sets.",
        "awakening": "Post-85 awakening greatly boosts AoE clear.",
        "tips": "Excellent for farming and speed runs."
    },
    "arme": {
        "name": "Arme",
        "role": "Mage / Support",
        "image": "https://picsum.photos/id/201/800/600",
        "description": "Powerful magic damage dealer and crowd control.",
        "leveling_tips": "Use area spells to clear packs quickly.",
        "job_path": "1st: Magician → 2nd: Wizard → 3rd: Archmage → 4th: Dimension Witch",
        "skill_recommend": "Max AoE spells and mana management skills.",
        "equipment": "Magic Attack and Skill Damage sets.",
        "awakening": "Unlock powerful new 4th bar skills.",
        "tips": "Strong in late-game content."
    },
    "ronan": {
        "name": "Ronan",
        "role": "Tank / Support",
        "image": "https://picsum.photos/id/251/800/600",
        "description": "Spell Knight with excellent defense and team buffs.",
        "leveling_tips": "Tanky playstyle, good for carrying new players.",
        "job_path": "1st: Spell Knight → 2nd: Holy Knight → 3rd: Rune Knight → 4th: Dragon Knight",
        "skill_recommend": "Focus on taunt and party buffs.",
        "equipment": "Defense and HP coordi.",
        "awakening": "Cheap filler until better DPS available.",
        "tips": "Build early for easy progression."
    },
    "jin": {
        "name": "Jin",
        "role": "Melee DPS",
        "image": "https://picsum.photos/id/1009/800/600",
        "description": "Fighter with high single-target damage.",
        "leveling_tips": "Strong in boss fights.",
        "job_path": "1st: Fighter → 2nd: Champion → 3rd: God of Martial Arts → 4th: Dragon Fist",
        "skill_recommend": "Combo skills and burst.",
        "equipment": "Attack Speed + Crit.",
        "awakening": "High priority for endgame.",
        "tips": "Fun and strong late-game."
    },
    "uno": {
        "name": "Uno",
        "role": "Versatile DPS",
        "image": "https://picsum.photos/id/870/800/600",
        "description": "Bloodless character – one of the strongest in current meta.",
        "leveling_tips": "Fastest clearer in the game.",
        "job_path": "Multiple jobs with excellent synergy.",
        "skill_recommend": "Max all damage skills.",
        "equipment": "Full Crit + Attack coordi.",
        "awakening": "Top priority after Lv85.",
        "tips": "Best character for new players in 2026 meta."
    },
    "amy": {
        "name": "Amy",
        "role": "Support / Buffer",
        "image": "https://picsum.photos/id/1003/800/600",
        "description": "Dancer that provides massive team damage buffs.",
        "leveling_tips": "Build after main DPS.",
        "job_path": "Dancer line",
        "skill_recommend": "Buff skills first.",
        "equipment": "Support coordi.",
        "awakening": "3★ priority.",
        "tips": "Essential for high-end content."
    },
    "sieghart": {
        "name": "Sieghart",
        "role": "Melee DPS",
        "image": "https://picsum.photos/id/133/800/600",
        "description": "Gladiator with powerful ultimate skills.",
        "leveling_tips": "Strong throughout all stages.",
        "job_path": "Gladiator line",
        "skill_recommend": "Ultimate and AoE.",
        "equipment": "Crit Damage sets.",
        "awakening": "Very strong post-awakening.",
        "tips": "Reliable all-rounder."
    }
}

@app.route("/")
def home():
    return render_template("index.html", characters=characters)

@app.route("/characters")
def characters_page():
    search = request.args.get("search", "").lower()
    filtered = {k: v for k, v in characters.items() if search in v["name"].lower()}
    return render_template("characters.html", characters=filtered)

@app.route("/character/<slug>")
def character_detail(slug):
    char = characters.get(slug)
    if not char:
        return "Character not found", 404
    return render_template("character_detail.html", char=char, slug=slug)

@app.route("/guides")
def general_guides():
    return render_template("general_guide.html")

@app.route("/api/characters")
def api_characters():
    return jsonify(characters)

if __name__ == "__main__":
    app.run(debug=True)