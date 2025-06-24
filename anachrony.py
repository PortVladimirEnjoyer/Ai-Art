import random

# Configuration - defines story parts and their markers
STORY_PARTS = {
    1: {"name": "Beginning", "markers": ["once upon a time", "in a kingdom", "long ago"]},
    2: {"name": "Problem", "markers": ["but one day", "suddenly", "disaster struck"]},
    3: {"name": "Action", "markers": ["decided to", "embarked on", "set out to"]},
    4: {"name": "Ending", "markers": ["in the end", "finally", "happily ever after"]}
}

def detect(paragraph):
    """Identify which story part a paragraph belongs to"""
    lower_para = paragraph.lower()
    for part_num, data in STORY_PARTS.items():
        if any(marker in lower_para for marker in data["markers"]):
            return part_num
    return None  # No match found

def assign(paragraphs):
    """Assign each paragraph to a story part"""
    analyzed = []
    for para in paragraphs:
        part_num = detect(para) or 1  # Default to Beginning (1) if no match
        analyzed.append({
            "text": para,
            "number": part_num,
            "name": STORY_PARTS[part_num]["name"]
        })
    return analyzed

def shuffle(analyzed_parts):
    """Randomize the order of parts"""
    # Create list of indices to shuffle
    indices = list(range(len(analyzed_parts)))
    random.shuffle(indices)
    
    # Return parts in new order
    return [analyzed_parts[i] for i in indices]

def output(shuffled_parts):
    """Format and print the rearranged story"""
    # Combine all paragraphs into one text
    story_text = " ".join(part["text"] for part in shuffled_parts)
    
    # Wrap to 70 characters per line
    from textwrap import fill
    print(fill(story_text, width=70))

# Example usage
story = """
Once upon a time, in a kingdom far away, there lived a wise king.
The kingdom was peaceful and prosperous for many years.
But one day, a terrible dragon attacked the villages.
The king decided to seek help from the ancient wizard.
After a long journey, the wizard gave him a magic sword.
In the end, the king defeated the dragon and peace returned.
The kingdom celebrated their brave king for many years.
""".strip()

# Pipeline execution
paragraphs = [p.strip() for p in story.split('\n') if p.strip()]
analyzed = assign(paragraphs)
shuffled = shuffle(analyzed)
output(shuffled)