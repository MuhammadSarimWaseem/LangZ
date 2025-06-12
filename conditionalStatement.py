import re

def parse_conditional(text):
    """
    Parse conditional statements in the format:
    either (condition) { code } or { code }
    """
    pattern = r'either\s*\((.*?)\)\s*\{(.*?)\}\s*or\s*\{(.*?)\}'
    
    matches = re.findall(pattern, text, flags=re.DOTALL)
    
    if matches:
        print("Match found!")
        return [(cond.strip(), then.strip(), else_.strip()) for cond, then, else_ in matches]
    else:
        print("No match found.")
        return None

def main():
    test_cases = [
        # Valid test cases
        'either (x > 5) { print("x is large") } or { print("x is small") }',
        'either (age < 18) { status = "minor" } or { status = "adult" }',
        'either (x == 1) {\n    console.log("One");\n} or {\n    console.log("Not One");\n}',

        # Invalid test cases
        'invalid (x > 5) { code } or { code }',
        'either (x > 5) print("x is large") or print("x is small")',
    ]

    for text in test_cases:
        print(f"\nTesting: {text}")
        result = parse_conditional(text)
        
        if result:
            for i, (cond, then, else_) in enumerate(result, 1):
                print(f"\nCondition #{i}:")
                print(f"Condition: {cond}")
                print(f"Then block: {then}")
                print(f"Else block: {else_}")
        else:
            print("Invalid conditional syntax")

if __name__ == '__main__':
    main()
