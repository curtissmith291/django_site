from typing import List
from django.shortcuts import render
import itertools

# Create your views here.

# --------------------
# Dictionaries/Lists
# --------------------

note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}

value_notes = {1: 'A', 2: 'A#/Bb', 3: 'B', 4: 'C', 5: 'C#/Db', 6: 'D', 7: 'D#/Eb', 8: 'E', 9: 'F', 
    10: 'F#/Gb', 11: 'G', 12: 'G#/Ab'}

string_values = {'E': 8, 'A': 1, 'D': 6, 'G': 11, 'B': 3, 'e': 8}

string_names = ['E', 'A', 'D', 'G', 'B', 'e']

string_counts = {'E': 0, 'A': 1, 'D': 2, 'G': 3, 'B': 4, 'e': 5}

# defining chord structures for types of chords
chord_structures = {
    "Major": ["Root", "Major Third", "Perfect Fifth"],
    "Minor": ["Root", "Minor Third", "Perfect Fifth"],
    "Diminished": ["Root", "Minor Third", "Diminished Fifth"],
}

# --------------------
# Defining Functions
# --------------------

def note_value(string, fret):
    '''
    This functon converts the fret number to a numerical note value
    '''
    note_num = string_values[string] + fret
    # checks if number is >12, if so, subtracts 12 until it's 12 or lower
    while True:
        if note_num > 12:
            note_num = note_num - 12
            continue
        else:
            break
    note = value_notes[note_num]
    return note

def note_to_fret(note_list):
    '''
    This function converts a list of notes representing a chord and returns the list as fret numbers up to fret 12.
    Example input -> ['--', 'C', 'E', 'G', 'C', 'E']
    Output -> ['--', 3, 2, 0, 1, 0]
    '''
    output = []
    for i in range(len(note_list)):
        if note_list[i] == '--':
            output.append('--')
            continue
        else:
            string_value = string_values[string_names[i]]
            note_value = note_values[note_list[i]]
            fret = note_value - string_value
            if fret < 0:
                fret += 12
            elif fret >= 12:
                fret -= 12
            output.append(fret)
    return output

def fret_in_range(fret_list, fret_range):
    '''
    This function checks if the fret numbers of the input chord are within the range specified
    '''
    check = []
    added_12 = False
    # creates a list of just fret numbers, removes "--"
    # Adds 12 to the frets if any frets are over 12 and note is lower than the min in fret range
    for i in fret_list:
        if i != '--':
            if max(fret_range) >= 12 and i < min(fret_range):
                added_12 = True
                check.append(i + 12)
            else:
                check.append(i)
    # cheks if chords are in the fret range
    if added_12 == False:
        if max(check) <= max(fret_range) and min(check) >= min(fret_range):
            return fret_list
    elif added_12 == True:
        if max(check) <= max(fret_range) and min(check) >= min(fret_range):
            fret_list_added = []
            for i in fret_list:
                if i == "--":
                    fret_list_added.append('--')
                elif i < min(fret_range):
                    fret_list_added.append(i + 12)
                else:
                    fret_list_added.append(i)
            return fret_list_added

# Function returns the degrees based on the user input root note
def degree_calculator(note):
    '''
    This function takes one input note (typically the root note) and returns a dictionary of the 12 degrees of the major scale.
    Input note needs to be an int.
    '''
    # converts note to numerical value
    note_values = {'A': 1, 'A#/Bb': 2, 'B': 3, 'C': 4, 'C#/Db': 5, 'D': 6, 'D#/Eb': 7, 'E': 8, 'F': 9, 
    'F#/Gb': 10, 'G': 11, 'G#/Ab': 12}
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


# --------------------
# Program starts below
# -------------------- 

# Views

# Input View
def chords_in_key_view(request):
    return render(request, 'chords_in_key.html')

# Error View
def chords_in_key_error_view(request):
    return render(request, 'chords_in_key_error.html')


# Result View
def chords_in_key_result_view(request):

    try:
        # user input values
        low_fret = int(request.GET['low'].strip())
        high_fret = int(request.GET['high'].strip())
        key = request.GET['key'].strip()

        # check that the low fret is lower than the high fret
        if high_fret <= low_fret:
            error_message = "The low fret entry needs to be less than the high fret entry"
            context = {"error": error_message}
            return render(request, 'chords_in_key_error.html', context)

        if high_fret - low_fret >5:
            error_message = "The fret range must be less than 6"
            context = {"error": error_message}
            return render(request, 'chords_in_key_error.html', context)

        fret_range = [low_fret, high_fret]

        root_note = key

        # STEP 3: Calculate degrees of root note; will need to do again for each degree
        dictionary_of_degrees = degree_calculator(root_note)

        # Create dictionary of major scale notes
        major_scale =   {
            "Root":dictionary_of_degrees["Root"],
            "Major Second":dictionary_of_degrees["Major Second"],
            "Major Third":dictionary_of_degrees["Major Third"],
            "Perfect Fourth":dictionary_of_degrees["Perfect Fourth"],
            "Perfect Fifth":dictionary_of_degrees["Perfect Fifth"],
            "Major Sixth":dictionary_of_degrees["Major Sixth"],
            "Major Seventh":dictionary_of_degrees["Major Seventh"]
        }

        # create dictionary of diatonic chords; this will be what is returned
        diatonic_chords = {
            dictionary_of_degrees["Root"]: {"degree": 1, "degree_r": "i", "note": dictionary_of_degrees["Root"], "type" : "Major", "structures": []},
            dictionary_of_degrees["Major Second"]: {"degree": 2, "degree_r": "ii", "note": dictionary_of_degrees["Major Second"],"type" : "Minor", "structures": []},
            dictionary_of_degrees["Major Third"]: {"degree": 3, "degree_r": "iii", "note": dictionary_of_degrees["Major Third"],"type" : "Minor", "structures": []},
            dictionary_of_degrees["Perfect Fourth"]: {"degree": 4, "degree_r": "iv", "note": dictionary_of_degrees["Perfect Fourth"],"type" : "Major", "structures": []},
            dictionary_of_degrees["Perfect Fifth"]: {"degree": 5, "degree_r": "v", "note": dictionary_of_degrees["Perfect Fifth"],"type" : "Major", "structures": []},
            dictionary_of_degrees["Major Sixth"]: {"degree": 6, "degree_r": "vi", "note": dictionary_of_degrees["Major Sixth"],"type" : "Minor", "structures": []},
            dictionary_of_degrees["Major Seventh"]: {"degree": 7, "degree_r": "vii", "note": dictionary_of_degrees["Major Seventh"],"type" : "Diminished", "structures": []},
        }



        # iterate through 7 notes in major scale
        for note in major_scale.values():
            # calculate degrees for note
            major_scale_degrees_dict = degree_calculator(note)
            # get chord type
            chord_type = diatonic_chords[note]["type"]
            # get chord structure
            structure = chord_structures[chord_type]
            # get notes for structure; i.e., the notes for the chord of the current root note
            structure_notes = []
            for item in structure:
                structure_notes.append(major_scale_degrees_dict[item])
            temp_root = structure_notes[0]

            # iterate though strings
            for string in string_names:
                # Note value of string
                value = string_values[string]
                # Number of string 0-5
                string_count = string_counts[string]

                # can't have chords made of one string, skipping last string as the root note
                if string_count == 5:
                    continue

                # initialize list of chords
                temp_chord_list = []
                current_chord_structure = []
                # create list contianing placement of the root note
                for i in range(0, string_count):
                    current_chord_structure.append("--")
                current_chord_structure.append(temp_root)
                
                remaining_note_list = [list(x) for x in itertools.product(structure_notes, repeat=(5 - string_count))]
                for item in remaining_note_list:
                    temp_chord_list.append(current_chord_structure + item)

                # checks that all the notes in the generated chord are in the chord structure             
                currated_list = []
                for item in temp_chord_list:
                    
                    # removes "--" from elements notes being checked against the notes in the chord
                    item_to_check = []
                    for element in item:
                        if element != "--":
                            item_to_check.append(element)

                    # checks that all the notes in the generated chord are in the chord structure
                    check = all([i in structure_notes for i in item_to_check]) and all([i in item_to_check for i in structure_notes])
                    if check == True:
                        currated_list.append(item)

                # convert lists of notes into lists of fret positions
                currated_list_values = []
                for item in currated_list:
                    currated_list_values.append(note_to_fret(item))

                # check if fret positions are within the range specified
                for item in currated_list_values:
                    check_chord = fret_in_range(item, fret_range)
                    if check_chord != None:
                        # append chord to final dictionary
                        diatonic_chords[temp_root]["structures"].append(check_chord)

        list_of_dicts = [x for x in diatonic_chords.values()]


        context =   {
            "diatonic_chords": diatonic_chords,
            "key": key,
            "low_fret": low_fret,
            "high_fret": high_fret,
            "list_of_dicts": list_of_dicts
        }

        return render(request, 'chords_in_key_results.html', context)


    except:
        error_message = "Uh oh, something went wrong, guess I need to test more..."
        context = {"error": error_message}
        return render(request, 'chords_in_key_error.html', context)