import parser
import codeWriter
import assemblyTable
import sys

def main():
    args = sys.argv
    output_file = args[1].split(".")[0] + ".asm"

    parser1 = parser.Parser(args[1])
    parser1.get_commands()
    parser1.rm_comments()
    parser1.rm_new_line()
    parser1.rm_blank_line()
    commands = parser1.commands

    codewriter = codeWriter.CodeWriter(commands)
    codewriter.translate()
    code = codewriter.code

    file = open(output_file, 'w')
    for line in code:
        file.write(line)
    file.close()

if __name__ == '__main__':
    main()

    
