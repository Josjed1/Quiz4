from module1 import function1 as math
from module2 import function2 as sentence
from module3 import function3 as both

def main():
    math.basicmath(6, 7)
    sentence.sentence_structure("Hello", "World")
    both.ambiguous("Hello", 7)
    
if __name__ == "__main__":
    main()
