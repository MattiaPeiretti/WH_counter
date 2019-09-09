import os
import json
import os.path

JSON_FILE_DIR = 'json/'

main_menu = '\n\n   s. Show redcords\n   a. Add record\n   q. Quit program\n\n'
running = True

try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def load_records(dir=JSON_FILE_DIR):
    recs = {}
    for filename in os.listdir(dir):
        if filename.endswith(".json"):
            with open(dir+filename) as data_file:
                data_loaded = json.load(data_file)
        recs[filename] = {'worked_hours': data_loaded['worked_hours'], 'earnings': data_loaded['earnings']}
    if recs == {}:
        return False
    else:
        return recs


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_records():
    ret = load_records()
    if ret:
        for key in ret.keys():
            print(key + '  ' + str(ret[key]['worked_hours']) + '  ' + str(ret[key]['worked_hours']*ret[key]['earnings']) + '  ' + str(ret[key]['earnings']))
    else:
        print('No records found')
    press_enter_to_continue()


def write_json(data, filename, filepath=JSON_FILE_DIR):
    if not os.path.exists(filepath + filename + '.json'):
        with open(filepath + filename + '.json', 'w', encoding='utf8') as outfile:
            json_str = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(json_str))
            return True
    else:
        return False


def press_enter_to_continue():
    input('\nPress <ENTER> key to continue...')


def add_record():
    cls()
    inp = input('Please enter the name of the record: ')
    name = inp
    inp = input('Enter the worked hours already worked: ')
    if inp.isdigit():
        inp = float(inp)
        worked_hours = inp
        inp = input('Enter the money earned per hour: ')
        if inp.isdigit():
            inp = float(inp)
            earnings = inp
            succes = write_json({'name': name,
                                 'worked_hours': worked_hours,
                                 'earnings': earnings}, name)
            if succes:
                print('File written succesfully!!')
                press_enter_to_continue()
            else:
                print('The file already exists!!')
                press_enter_to_continue()


while running:
    cls()
    print(main_menu)
    inp = input('Please, select an option: ')
    if inp == 's':
        show_records()
    elif inp == 'a':
        add_record()
    elif inp == 'q':
        running = False
    else:
        cls()
        print('Command not recognized, please try again!')
        press_enter_to_continue()
