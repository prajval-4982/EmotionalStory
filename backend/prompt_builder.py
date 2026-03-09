from dataset_utils import extract_emotion_style

def build_chat_messages(seed, emotion, strength):
    # Get the (possibly blended) style
    style = extract_emotion_style(emotion)
    
    # SYSTEM PROMPT
    system_content = f"""
You are an expert literary fiction writer known for psychological realism.

YOUR GOAL: 
Write a short story (400-800 words) that evokes the complex emotional state of: "{emotion}".

CRITICAL RULES:
1. **Show, Don't Tell:** Never name the emotions directly. 
2. **The Conflict:** If two emotions are listed, focus on the TENSION between them.
3. **Vocabulary:** Avoid repetition.
4. **Pacing:** {style['pace']}

STYLE GUIDE:
- Imagery: {style['imagery']}
- Dialogue: {style['dialogue']}

ENDING:
- End with a lingering thought or physical action.
""".strip()

    # USER PROMPT
    user_content = f"""
**STORY SEED:** "{seed}"
**EMOTION:** {emotion}
**INTENSITY:** {strength}/10

**INSTRUCTIONS:**
- Focus on the physical texture of objects.
- Allow the conflicting emotions to bleed into the description of the setting.
- Write the story now.
""".strip()

    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]