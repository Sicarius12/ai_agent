from functions.get_files_info import get_files_info
from functions.get_files_info import get_files_info_alt

# print(get_files_info("calculator", "."))
# print(get_files_info("calculator", "pkg"))
# print(get_files_info("calculator", "/bin"))
# print(get_files_info("calculator", "../"))
# print(get_files_info("calculator", "../"))

print(f'Mine: {get_files_info("calculator", "../calculator_tmp")}')
print(f'Solution: {get_files_info_alt("calculator", "../calculator_tmp")}')

print(f'Mine: {get_files_info("calculator", "../calculator_backup")}')
print(f'Solution: {get_files_info_alt("calculator", "../calculator_backup")}')