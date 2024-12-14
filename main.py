import re


def get_word_count_and_avg_sentence_length(Moby_Dick_Chapter_1):
    word_count = {}
    total_sentence_length = 0
    total_sentences = 0

    with open('Moby_Dick_Chapter_1.txt', 'r') as input_file:
        for line in input_file:

            line = line.lower()

            line_clean = re.sub(r'[^\w\s]', '', line)

            line_split = line_clean.split()

            for word in line_split:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1


            sentences = line.split('.')
            total_sentences += len(sentences) - 1
            total_sentence_length += sum(len(s.split()) for s in sentences[:-1])

    avg_sentence_length = total_sentence_length / total_sentences if total_sentences else 0
    return word_count, avg_sentence_length



word_count, avg_sentence_length = get_word_count_and_avg_sentence_length('Moby_Dick_Chapter_1.txt')
print(f"Word 'old' count in Moby Dick: {word_count.get('old', 0)}")
print(f"Word 'water' count in Moby Dick: {word_count.get('water', 0)}")
print(f"Average sentence length in Moby Dick: {avg_sentence_length}")


