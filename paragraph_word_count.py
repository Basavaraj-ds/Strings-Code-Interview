
def paragraphcount(paragraph):
    paragraph = paragraph.split()
    dict = {}

    for i in paragraph:
        i = i.strip("!@#$%^").lower()
        dict[i] = paragraph.count(i)
    return dict

paragraph= "Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."

para =paragraphcount(paragraph)
print(para)

