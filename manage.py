import util
import sys
if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "build":
        print("Build was specified")
        util.populate_dict()
        util.update_pages()
    elif command == "new":
        print("New page was specified")
        util.new_page()
    else:
        print("Please specify ’build’ or ’new’")
    
else:
    print('Invalid command: please select \'build\' or \'new\'')

