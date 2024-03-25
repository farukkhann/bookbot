def main():    
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        book_text_str = str(file_contents)
        count_alpha_dict = count_alpha_count(book_text_str)
        refined_data = orgainise_data(count_alpha_dict)
        sorted_refined_data = sort_data(refined_data)
        print_final_output(sorted_refined_data)
        # print(sorted_refined_data)
        # ...

def count_words(text_string):
    words_arr = text_string.split()
    words = len(words_arr)
    print(words)

def count_alpha_count(text_string):
    count_record = {}
    text_string = text_string.lower()
    for alpha in text_string:
        # print(count_record.get("name"))
        if(alpha.isalpha()):
            if(not count_record.get(alpha)):
                count_record[alpha] = 1
            else:
                count_record[alpha] = count_record[alpha]+1
    return count_record
# count_alpha_count("farukkK")

def orgainise_data(count_record_dict):
    data = []
    for alpha in count_record_dict:
        data.append({
            "name": alpha,
            "count":count_record_dict[alpha]
        })
    return data

def sort_data(name_count_data):
    return sorted(name_count_data,key=lambda x:x['count'], reverse=True)

def print_final_output(data):
    for entry in data:
        print(f'The {entry['name']} character was found {entry["count"]} times')
main()