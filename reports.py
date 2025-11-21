# File          : reports.py
# Author        : Jorge Ortega
# Email id      : ortjy007@mymail.unisa.edu.au
# Description   : COMP 1048 advanced-oop-and-testing Assignment 2
#
# This is my own work as defined by the University's
# Academic Misconduct policy.

import print_report


def basic_typing_menu() -> list:
    """
    Basic note/comment menu for use interface
    :return:
    """
    # Basic note/comment input menu for use interface
    menu = {'A': 'to add note',
            'R': 'to replace a note',
            'D': 'to delete a note',
            'E': 'E to exit',
            }
    print(f'Please select from the menu below:')
    print_report.print_c(menu)

    # Building option list and return to be used for validation
    menu_keys = menu.keys()
    valid_options = list(menu_keys)

    return valid_options


def replace_delete_validation(comment_key, action='replace') -> str:
    """
    Validating note/comment to the replaced or deleted
    :param action: note or comment depending on use: str
    :param comment_key: list
    """
    # Identifying and validating comments to be repaced or deleted
    while True:
        try:
            rep_comment = input(f'Please select the note to '
                                f'be {action} or 0 to exit: ')
            if rep_comment not in comment_key:
                print(f'Invalid input please try again.')
            elif rep_comment == 'E' or rep_comment == '0':
                break
            else:
                break
        except ValueError:
            print(f'Invalid input.Only existing notes are allowed.')

    return rep_comment


def printing_section(working_section) -> None:
    """
    Simple method for printing report sections
    :param working_section:
    """
    for key in working_section:
        print(f'{key}: {working_section[key]}')
    print()


def updating_keys(report, append_file=None) -> list:
    """
    Rebuilding keys for note/comment identification
    :param append_file: append file if required
    :param report: dict
    :return: list
    """
    # Updating key list
    if append_file is None:
        comment_key = []
    else:
        comment_key = append_file

    for key in report:
        simple_k = str(key).replace('[', '').replace(']', '')
        comment_key.append(simple_k)

    # Adding exit value
    comment_key.append('0')

    return comment_key


def key_assembly(section: int, comment_no: int) -> float:
    """
    Building keys for report sections
    :param section:
    :param comment_no:
    :return: float
    """
    # Building a key
    key = str(section) + '.' + str(comment_no)
    key = float(key)
    return key


def typing(comment: list, label='comment') -> str:
    """
    Used to add comments/notes to reports
    :param comment: working list with comments
    :param label: text to appear in user interface
    """
    print(f'New {label} (please press \x1B[3menter\x1B[0m twice to finish):')
    while True:
        line = input()
        if line != '':
            comment.append(line)
        else:
            break
    final_comment = ' '.join(comment)
    return final_comment


def formats_available(report_number) -> dict:
    """
    Select a report with a pre-established structure (dict)
    :return: dict
    """

    # Dictionary of available formats for selection
    available_reports = {1: 'Simple Notes',
                         2: 'Animals Report',
                         3: 'Animals Health Report',
                         4: 'Enclosures Report',
                         5: 'Staffing Report',
                         6: 'Operations Report',
                         7: 'Events Report'
                         }

    # List to check section selection (starting at 1 and adding
    # one more as values start at 0)
    list_of_reports = []
    for i in range(len(available_reports) + 1):
        list_of_reports.append(i)



    # Dictionaries for initiating reports
    container = []

    # Generic Report
    r1 = {1: {0: 'Topic 1'},
          2: {0: 'Topic 2'},
          3: {0: 'Topic 3'},
          4: {0: 'Topic 4'},
          5: {0: 'Topic 5'}
          }
    container.append(r1)

    # Animals Report
    r2 = {1: {0: 'Animal Inventory'},
          2: {0: 'On/Off Exhibits'},
          3: {0: 'Ill/Injured'},
          4: {0: 'Special Attention'},
          5: {0: 'On Loan'},
          6: {0: 'In Isolation'},
          7: {0: 'Other'}
          }
    container.append(r2)

    # Animals Health Report
    r3 = {1: {0: 'General Health'},
          2: {0: 'Vaccinations / Preventive Medicine'},
          3: {0: 'Illnesses'},
          4: {0: 'Injuries'},
          5: {0: 'Accidents'},
          6: {0: 'Behavioral Issues'},
          7: {0: 'Other'}
          }
    container.append(r3)

    # Enclosures Report
    r4 = {1: {0: 'Enclosure Inventory'},
          2: {0: 'On/Off line'},
          3: {0: 'Occupied'},
          4: {0: 'Available'},
          5: {0: 'Being Refurbished'},
          6: {0: 'Decommissioned'},
          7: {0: 'Other'}
          }
    container.append(r4)

    # Staffing Report
    r5 = {1: {0: 'Staffing'},
          2: {0: 'By Role'},
          3: {0: 'By Department'},
          4: {0: 'Animal Care'},
          5: {0: 'External'},
          6: {0: 'Other'}
          }
    container.append(r5)

    # Operations Report
    r6 = {1: {0: 'Cleaning'},
          2: {0: 'Maintenance'},
          3: {0: 'Grounds'},
          4: {0: 'Special Events'},
          5: {0: 'Other'}
          }
    container.append(r6)

    # Events Report
    r7 = {1: {0: 'Recurring'},
          2: {0: 'Seasonal'},
          3: {0: 'Special'},
          4: {0: 'Last Minute'},
          5: {0: 'Other'}
          }
    container.append(r7)

    # Preliminary value
    selected_report = ''

    # If no report is requested as default:
    if report_number not in list_of_reports:

        # Information for user
        print(f'\nAvailable reports:')
        print_report.print_n(available_reports)

        # Validating section selection
        while selected_report != 0:
            try:
                selected_report = int(input(f'Please select between '
                                            f'1-{len(available_reports)} or 0 to Exit: '))
                if selected_report not in list_of_reports:
                    print(f'Invalid input please try again.')
                    print(list_of_reports)
                elif selected_report == 0:
                    print(f"Closing Application\n")
                    break
                else:
                    break
            except ValueError:
                print(f'Invalid input. Only integers are allowed.')

        # list start at zero minus one to match printed list
        return container[(selected_report - 1)]

    else:
        # list start at zero minus one to match printed list
        return container[report_number - 1]


def basic_report(title: str, name: '', b_format: {}) -> dict:
    """
    Creating a report using a Dictionary as storage
    :return: Dict
    """
    # Setting method lists and variables
    comment = []
    comment_key = []
    option = 'A'

    # Checking if a previous format or report is given
    # otherwise use an empty dictionary
    if b_format is None:
        b_report = {}
    else:
        b_report = b_format

    # Identifying the number of comments
    comment_no = len(b_report)

    # Printing existing comments
    print(f"{name}'s {title}'s notes:")
    print_report.print_n(b_report)
    print('Please be aware that notes are recorded progressively\n'
          'therefore numbers are sequentially updated even if a\n'
          'note is deleted.\n')

    # While loop to control comment options (adding, replacing,
    # deleting and exiting)
    while option != 'E':

        # Options Menu and valid options list
        valid_options = basic_typing_menu()

        # Requesting user input
        option = input('Your option: ')

        # Adding comments to the working section
        if option == 'A':
            # Printing for user information
            print(f"{name}'s {title}'s notes:")
            print_report.print_n(b_report)

            # Typing comments
            final_comment = typing(comment, 'note')
            comment_no += 1

            # Adding comments to report
            b_report[comment_no] = final_comment
            print(f"The following note has been added to {name}'s "
                  f"{title}'s report:")
            print_report.print_b(b_report)

            # Resetting WIP comment list
            comment = []

        # Replacing comments
        if option == 'R':

            # Printing for user information
            print(f'The following notes can be replaced:')
            for key in b_report:
                print(f'{key} {b_report[key]}')
                comment_key.append(str(key))

            # Adding exit value
            comment_key.append('0')

            # Identifying and validating comments to be replaced
            rep_comment = replace_delete_validation(comment_key, 'replaced')

            # Terminating input by user request
            if rep_comment == '0':
                print('Nothing replaced.\n')
            else:
                # Typing new comment to the working section
                final_comment = typing(comment, 'note')

                # Replacing comment in working dictionary
                tmp_key = int(rep_comment)
                b_report[tmp_key] = final_comment

                print(f"The following note has been replaced in {name}'s "
                      f"{title}:\n{tmp_key} {b_report[tmp_key]}\n")

                # Updating key list
                comment_key = updating_keys(b_report)

                # Resetting WIP comment list
                comment = []

        # Deleting comments
        if option == 'D':

            # Printing for user information
            print(f'The following notes can be replaced:')
            for key in b_report:
                print(f'{key} {b_report[key]}')
                comment_key.append(str(key))

            # Adding exit value
            comment_key.append('0')

            # Identifying and validating comments to be deleted
            rep_comment = replace_delete_validation(comment_key, 'deleted')

            # Terminating input by user request
            if rep_comment == '0':
                print('Nothing deleted.\n')
            else:
                # Deleting comment from working dictionary
                tmp_key = int(rep_comment)
                deleted_comment = b_report[tmp_key]
                del b_report[tmp_key]

                print(f"The following note has been deleted from {name}'s "
                      f"{title}:\n{tmp_key} {deleted_comment}\n")

                # Updating key list
                comment_key = updating_keys(b_report)

                # Resetting WIP comment list
                comment = []

        # Exiting comments
        if option == 'E':
            print_report.print_c(b_report)
            print(f"Closing {name}'s {title}'s notes.\n")

        # Validating selection:
        if option not in valid_options:
            option = input(f'Invalid input please try again:')

    return b_report


def extended_report(name: '', e_format: {}, topic='Generic Report') -> dict:
    """
    Creating a health report using a Dictionary as storage
    :return: Dict
    """
    # Setting methods lists and variables
    # Initial first section for any report
    section = 1

    # Working list of comments
    comment = []

    # Number of comments collected
    comment_no = 0

    # WIP dictionary
    working_section = {}

    # WIP comments
    working_comments = []

    # Import report format
    if e_format == {}:
        e_report = formats_available(1)
    else:
        e_report = e_format

    # List to check section selection (starting at 1 and adding
    # one more as values start at 0)
    existing_sections = [i for i in range(len(e_report) + 1)]

    # While loop to control input in report sections
    while section != 0:

        # Printing for user information
        print(f"\n{name}'s {topic} has the following sections:")
        print_report.print_n(e_report)
        print('Please note that comments are recorded progressively\n'
              'therefore numbers are sequentially updated even if a\n'
              'note is deleted.')

        # Validating section selection
        while True:
            try:
                section = int(input(f'Please select between '
                                    f'1-{len(e_report)} or 0 to Exit: '))
                if section not in existing_sections:
                    print(f'Invalid input please try again.')
                elif section == 0:
                    option = 'E'
                    print(f"Closing {name}'s {topic} Report.\n")
                    break
                else:
                    option = 'A'
                    break
            except ValueError:
                print(f'Invalid input. Only integers are allowed.')

        # While loop to control comment options (adding, replacing,
        # deleting and exiting)
        while option != 'E':

            # Adding comments user instructions
            print(f'\nAdding comments to Section {section}{str(e_report[section])
                  .replace('{', '').replace('}', '')
                  .replace('0', '').replace(':', '')
                  .replace("'", '')}.')

            # Options Menu and valid options list
            basic_typing_menu()

            # Requesting user input
            option = input('Your option: ')

            # Adding comments to the working section
            if option == 'A':
                # Printing for user information
                print(f"The following comments are in {name}'s {topic}:")
                printing_section(working_section)

                # Typing new comment to the working section
                final_comment = typing(comment, 'comment')

                # U Updating comment counter
                comment_no += 1

                # Building a key
                key = key_assembly(section, comment_no)

                # Inserting comment in working section
                working_section[key] = final_comment

                # User printing update
                print(f"The following comment has been added to {name}'s "
                      f"{topic}:")
                print_report.print_n(working_section)

                # Updating key list
                working_comments = updating_keys(working_section, working_comments)

                # Resetting WIP comment list
                comment = []

            # Replacing comments
            if option == 'R':
                # Printing for user information
                print(f'The following comments can be replaced:')
                printing_section(working_section)

                # Identifying and validating comments to be replaced
                print(f'New comment (please press \x1B[3menter\x1B[0m twice to finish):')
                rep_comment = replace_delete_validation(working_comments, 'replaced')

                # Terminating input by user request
                if rep_comment == '0':
                    print('Nothing replaced.\n')
                else:
                    # Typing new comment
                    final_comment = typing(comment, 'comment')

                    # Replacing comment in working dictionary
                    tmp_key = float(rep_comment)
                    working_section[tmp_key] = final_comment
                    print(f"The following comment has been replaced in {name}'s "
                          f"{topic}:\n{tmp_key} {working_section[tmp_key]}")

                    # Updating key list
                    working_comments = updating_keys(working_section, working_comments)

                    # Resetting WIP comment list
                    comment = []

            # Deleting comments
            if option == 'D':
                # Printing for user information
                print(f'The following comments can be deleted:')
                printing_section(working_section)

                # Identifying and validating comments to be replaced
                rep_comment = replace_delete_validation(working_comments, 'deleted')

                # Terminating input by user request
                if rep_comment == '0':
                    print('Nothing deleted.\n')
                else:
                    # Deleting comment from working dictionary
                    tmp_key = float(rep_comment)
                    deleted_comment = working_section[tmp_key]
                    del working_section[tmp_key]

                    print(f"The following comment has been deleted from {name}'s "
                          f"{topic}:\n{tmp_key} {deleted_comment}")

                    # Updating key list
                    updating_keys(working_section)

                    # Resetting WIP comment list
                    comment = []

            # Exiting comments
            if option == 'E':
                # Inserting new comments in dictionary
                e_report[section] = working_section

                # Resetting the working section
                working_section = {}
                print('Closing current section.\n')

    return e_report

# f = formats_available(3)
#e = extended_report('Oki', 'Generic')
#b = basic_report('Health Report', 'oki', {})
