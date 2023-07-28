def preprocess(text):
    # Preprocess the text
    text = text.replace("\\n", "")
    text = text.replace('\\xe2', '')
    text = text.replace('\\x80', '')
    text = text.replace('\\x99', '')
    text = text.replace('\\x98', '')
    text = text.replace('\\x9c', '')
    text = text.replace('\\x9d', '')
    text = text.replace('\\x9e', '')
    text = text.replace('\\xc3', '')
    text = text.replace('\\xa9', '')
    return text

if __name__ == '__main__':
    # read the txt file
    with open('marvel_dataset_txt/marvel_dataset.txt', 'r') as f:
        text = f.read()
        f.close()

    # length of text is the number of characters in it
    print(len(text))

    text = preprocess(text)

    # write the txt file
    with open('marvel_dataset_txt/marvel_dataset_preprocess.txt', 'w') as f:
        f.write(text)
    
