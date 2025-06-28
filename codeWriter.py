import assemblyTable
import parser

class CodeWriter:
    def __init__(self,commands):
        self.commands = commands
        self.code = []


    def translate(self):
        arithmetic_ops = ['add', 'sub', 'and', 'or', 'not', 'neg', 'eq', 'gt', 'lt']
        compare_ops = ['eq', 'gt', 'lt']
        compare_counter = 1
        LATT = ['local','argument','this','that']
        for command in self.commands:
            self.code.append("// " + command + "\n")
            eles = command.split(' ',2)
            if (eles[0] in arithmetic_ops) :
                key = eles[0]
                assembly_code = assemblyTable.map[key]
                assembly_code = assembly_code.replace('SP','0')
                if (key in compare_ops):
                    assembly_code = assembly_code.replace('{}',str(compare_counter))
                    compare_counter += 1
                self.code.append(assembly_code)
            else:
                if (eles[1] in LATT):
                    if(eles[1] =="local"):
                        key = eles[0]+' '+'segment'+' i'
                        assembly_code = assemblyTable.map[key].replace('segmentPointer','1')
                        assembly_code = assembly_code.replace('i',eles[2])
                    if(eles[1] =="argument"):
                        key = eles[0]+' '+'segment'+' i'
                        assembly_code = assemblyTable.map[key].replace('segmentPointer','2')
                        assembly_code = assembly_code.replace('i',eles[2])
                    if(eles[1] =="this"):
                        key = eles[0]+' '+'segment'+' i'
                        assembly_code = assemblyTable.map[key].replace('segmentPointer','3')
                        assembly_code = assembly_code.replace('i',eles[2])
                    if(eles[1] =="that"):
                        key = eles[0]+' '+'segment'+' i'
                        assembly_code = assemblyTable.map[key].replace('segmentPointer','4')
                        assembly_code = assembly_code.replace('i',eles[2])
                
                elif eles[1] == "pointer":
                    key = f"{eles[0]} pointer {eles[2]}"
                    assembly_code = assemblyTable.map[key]
                else:
                    key = eles[0]+' '+eles[1]+' i'                              
                    assembly_code = assemblyTable.map[key].replace('i',eles[2])
                assembly_code = assembly_code.replace('SP','0')
                self.code.append(assembly_code)
            
            