# Making imports
from cw_3_virt_env.utils.utils import (json_load, sort_last_five_list,
                                       final_information)

# Assigning variables
all_operation_list = json_load("../../operations.json")
last_five_sorted = sort_last_five_list(all_operation_list)
final_information_list = final_information(last_five_sorted)

# Printing last five formed operations
for operation in final_information_list:
    print(operation)
