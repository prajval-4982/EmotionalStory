def extract_emotion_style(emotions_str):
    """
    Parses a comma-separated string of emotions (e.g., "Happy, Sad") 
    and returns a blended style guide.
    """
    if not emotions_str:
        emotions_str = "sad"

    # 1. Split the string into a list
    emotions = [e.strip().lower() for e in emotions_str.split(",")]
    
    # Define the base styles
    styles = {
        "sad": {
            "pace": "slow, methodical, and heavy",
            "imagery": "cold, grey, shadows, rain, decay",
            "dialogue": "sparse, unspoken words, lingering silence"
        },
        "happy": {
            "pace": "upbeat, flowing, and rhythmic",
            "imagery": "warm light, vibrant colors, open spaces, nature",
            "dialogue": "enthusiastic, connecting, fast-paced"
        },
        "fear": {
            "pace": "erratic, tense, with sudden stops",
            "imagery": "darkness, confinement, blurred vision, sharp sounds",
            "dialogue": "whispered, stuttered, or breathless"
        },
        "anger": {
            "pace": "fast, aggressive, driving forward",
            "imagery": "heat, red, breakage, tightness, boiling",
            "dialogue": "sharp, accusatory, loud, cutting"
        },
        "curiosity": {
            "pace": "wandering, investigative, steady",
            "imagery": "light through cracks, dust motes, textures, hidden details",
            "dialogue": "questioning, contemplative"
        },
        "hope": {
            "pace": "rising, steady, looking forward",
            "imagery": "dawn, horizons, clearing skies, sturdy objects",
            "dialogue": "gentle, reassuring, future-tense"
        }
    }

    # 2. If it's just one emotion
    if len(emotions) == 1:
        return styles.get(emotions[0], styles["sad"])

    # 3. If it's MIXED emotions
    e1 = emotions[0]
    e2 = emotions[1] if len(emotions) > 1 else e1
    
    style1 = styles.get(e1, styles["sad"])
    style2 = styles.get(e2, styles["sad"])

    return {
        "pace": f"A complex rhythm, shifting between {style1['pace']} and {style2['pace']}.",
        "imagery": f"A contrast of opposites: blend {style1['imagery']} with elements of {style2['imagery']}.",
        "dialogue": f"Layered subtext. Surface: {style1['dialogue']}, but underneath: {style2['dialogue']}."
    }