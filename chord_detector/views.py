from django.shortcuts import render

# --------------------
# Dictionaries/lists to convert notes to numbers/numebers to notes
# --------------------
note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
    10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

string_value = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

string_names = ['E', 'A', 'D', 'G', 'B', 'e']


# --------------------
# Defining functions
# --------------------

# Function to convert fret numbers to notes
def note_value(string, fret):
    '''
    This functon converts the fret number to a numerical note value
    '''
    note_num = string_value[string] + fret
    # checks if number is >12, if so, subtracts 12 until it's 12 or lower
    while True:
        if note_num > 12:
            note_num = note_num - 12
            continue
        else:
            break
    note = value_notes[note_num]
    return note


# # Checks input for empty (muted) strings, assigns them '--', assigns notes to input values
def note_converter(list_to_check):
    '''
    This funtion iterates through input fret values and assigns note to numerical inputs and '--' to muted strings
    '''
    string_count = 0
    inputs_fret_values = []
    for item in list_to_check:
        if type(item) is int:
            inputs_fret_values.append(note_value(string_names[string_count], item))
            string_count += 1
        else:
            inputs_fret_values.append("--")
            string_count += 1
    list_of_input_notes = [x for x in inputs_fret_values if x != "--"]
    root = list_of_input_notes[0]
    return inputs_fret_values, list_of_input_notes, root

# Function returns the degrees based on the user input root note
def degree_calculator(note):
    '''
    This function takes one input note (typically the root note) and returns a dictionary of the 12 degrees of the major scale
    '''

    value = note_values[note]

    root = note

    minor_second_num = value + 1
    if minor_second_num > 12:
        minor_second_num -= 12
    minor_second = value_notes[minor_second_num]

    major_second_num = value + 2
    if major_second_num > 12:
        major_second_num -= 12
    major_second = value_notes[major_second_num]

    minor_third_num = value + 3
    if minor_third_num > 12:
        minor_third_num -= 12
    minor_third = value_notes[minor_third_num]

    major_third_num = value + 4
    if major_third_num > 12:
        major_third_num -= 12
    major_third = value_notes[major_third_num]

    perfect_fourth_num = value + 5
    if perfect_fourth_num > 12:
        perfect_fourth_num -= 12
    perfect_fourth = value_notes[perfect_fourth_num]

    dim_fifth_num = value + 6
    if dim_fifth_num > 12:
        dim_fifth_num -= 12
    dim_fifth = value_notes[dim_fifth_num]

    perfect_fifth_num = value + 7
    if perfect_fifth_num > 12:
        perfect_fifth_num -= 12
    perfect_fifth = value_notes[perfect_fifth_num]

    aug_fifth_num = value + 8
    if aug_fifth_num > 12:
        aug_fifth_num -= 12
    aug_fifth = value_notes[aug_fifth_num]

    minor_sixth_num = value + 8
    if minor_sixth_num > 12:
        minor_sixth_num -= 12
    minor_sixth = value_notes[minor_sixth_num]

    major_sixth_num = value + 9
    if major_sixth_num > 12:
        major_sixth_num -= 12
    major_sixth = value_notes[major_sixth_num]

    minor_seventh_num = value + 10
    if minor_seventh_num > 12:
        minor_seventh_num -= 12
    minor_seventh = value_notes[minor_seventh_num]

    major_seventh_num = value + 11
    if major_seventh_num > 12:
        major_seventh_num -= 12
    major_seventh = value_notes[major_seventh_num]

    degrees =  [root, minor_second, major_second, minor_third, major_third, perfect_fourth, dim_fifth, 
                perfect_fifth, aug_fifth, minor_sixth, major_sixth, minor_seventh, major_seventh]

    degree_strings =    ["Root", "Minor Second", "Major Second", "Minor Third", "Major Third", "Perfect Fourth", 
                        "Diminished Fifth", "Perfect Fifth", "Augmented Fifth", "Minor Sixth", "Major Sixth", 
                        "Minor Seventh", "Major Seventh"]

    dictionary_of_degrees = dict(zip(degree_strings, degrees))

    return dictionary_of_degrees

def chord_detector(root, list_of_notes, dictionary_of_chords):
    '''
    This function takes three arguments: root note, the list of user input notes, and the dictionary of chords.
    The dictionary is iterated through; if the dictionary notes and the input notes perfectly match, a chord is found; 
    else, the iteration continues. 
    If no match is found, "Input notes do not match a chord" is returned. 

    **Note** This function ONLY returns chords in which the root note is part of the chord. Some chord shortcuts remove the 
    root note to make the chord easier to play: this function will not recognize those chords. 
    '''
    counter = 0
    for item in dictionary_of_chords.items():
        check = all([i in list_of_notes for i in item[1]]) and all([i in item[1] for i in list_of_notes])
        if check == True:
            # print(f'{root_note} {item[0]} chord')
            result = (f'{root} {item[0]} chord')
            return result
        if check == False:
            counter += 1
            if counter == len(dictionary_of_chords):
                # print("Input notes do not match a chord")
                result = ("Input notes do not match a chord")
                return result
            else: 
                continue

# --------------------
# Program starts below
# --------------------

# Views

# Input View
def chord_views(request):
    return render(request, 'chords.html')

# Result View
def sf_results_view(request):

    try:

        # user input values
        string_low_e = request.GET['E'].strip()
        string_a = request.GET['A'].strip()
        string_d = request.GET['D'].strip()
        string_g = request.GET['G'].strip()
        string_b = request.GET['B'].strip()
        string_high_e = request.GET['e'].strip()

        # Combines inputs into list for manipulation
        string_list = [string_low_e, string_a, string_d, string_g, string_b, string_high_e]

        # Checks input for empty (muted) strings, assigns them '--'
        input_notes, note_list, root_note = note_converter(string_list)

        # Creating a dictionary of the degrees based of the user input root note
        degree_dictionary = degree_calculator(root_note)

        # loop to return chord structures based of dictionary
        for item in degree_dictionary.items():
            major_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"]]
            minor_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"]]
            augmented_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Augmented Fifth"]]
            diminished_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Diminished Fifth"]]
            fifth_chord = [degree_dictionary["Root"], degree_dictionary["Perfect Fifth"]]
            suspended4_chord = [degree_dictionary["Root"], degree_dictionary["Perfect Fourth"], degree_dictionary["Perfect Fifth"]]
            suspended2_chord = [degree_dictionary["Root"], degree_dictionary["Major Second"], degree_dictionary["Perfect Fifth"]]
            major_sixth_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Sixth"]]
            minor_sixth_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Sixth"]]
            dominant_seventh_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Minor Seventh"]]
            major_seventh_chord = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Seventh"]]
            minor_seventh_chord = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Minor Seventh"]]
            minor_major_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Perfect Fifth"], degree_dictionary["Major Seventh"]]
            augmented_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Major Third"], degree_dictionary["Augmented Fifth"], degree_dictionary["Minor Seventh"]]
            diminished_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Diminished Fifth"], degree_dictionary["Major Sixth"]]
            half_diminished_seventh_chords = [degree_dictionary["Root"], degree_dictionary["Minor Third"], degree_dictionary["Diminished Fifth"], degree_dictionary["Minor Seventh"]]

            # # Create a dictionary of the lists of chord notes
            chord_list = [major_chord, minor_chord, augmented_chord, diminished_chord, fifth_chord, suspended4_chord, suspended2_chord, major_sixth_chord, minor_sixth_chord, 
                dominant_seventh_chord, major_seventh_chord, minor_seventh_chord, minor_major_seventh_chords, augmented_seventh_chords, diminished_seventh_chords, 
                half_diminished_seventh_chords]
            chord_strings = "Major, Minor, Augmented, Diminished, 5/Power, sus4, sus2, 6, m6, 7, maj7, m7, m(maj)7, 7(#5) (minor-major seventh), dim7, m7(b5) (half-diminished seventh)"
            chord_strings = chord_strings.split(", ")
            chord_dictionary = dict(zip(chord_strings, chord_list))

            result = chord_detector(root_note, note_list, chord_dictionary)

            context = {"result": result, "chord_structures": chord_dictionary, "degrees": degree_dictionary}

            return render(request, 'chords_results.html', context)

    except:

        result = "Uh oh, something went wrong..."
        context = {"result": result}
    
        return render(request, 'chords_results.html', context)