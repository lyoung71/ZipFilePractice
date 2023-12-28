#! python3

# copies an entire folder and its contents into
# a zip file whose filename increments.

import zipfile, os


def backup_to_zip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    print(f'Creating {zip_filename}...')

    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backup_zip.write(foldername)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done.')

backupToZip('/Users/landonyoung/Programming/fun')
