import assemblyTable
import parser

class CodeWriter:
    def __init__(self,commands):
        self.arithmetic_ops = ['add', 'sub', 'and', 'or', 'not', 'neg', 'eq', 'gt', 'lt']
        self.compare_ops = ['eq', 'gt', 'lt']
        self.LATT = ['local','argument','this','that']
        self.commands = commands
        self.code = []
        self.compare_counter = 1

    def isMemory(self,eles):
        if (eles[0] == "push" or eles[0] == "pop"):
            return True
        
    def isArithmetic(self,eles):
        if (eles[0] in self.arithmetic_ops):
            return True
        
    def isLATT(self,eles):
        if (eles[1] in self.LATT):
            return True
        
    def isCompare(self,eles):
        if (eles[0] in self.compare_ops):
            return True
        
    def translateLATT(self,eles):
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
        return assembly_code

    def translateOthers(self,eles):
        if eles[1] == "pointer":
            key = f"{eles[0]} pointer {eles[2]}"
            assembly_code = assemblyTable.map[key]
        else:
            key = eles[0]+' '+eles[1]+' i'                              
            assembly_code = assemblyTable.map[key].replace('i',eles[2])
        return assembly_code

    def translateArithmetic(self,eles):
        key = eles[0]
        assembly_code = assemblyTable.map[key]
        if (key in self.compare_ops):
            assembly_code = assembly_code.replace('{}',str(self.compare_counter))
            self.compare_counter += 1
        return assembly_code

    def translate(self):
        for command in self.commands:
            self.code.append("// " + command + "\n")
            eles = command.split(' ',2)
            if (self.isArithmetic(eles)) :
                assembly_code = self.translateArithmetic(eles)
            else:
                if (self.isLATT(eles)):
                    assembly_code = self.translateLATT(eles)
                else:
                    assembly_code = self.translateOthers(eles)
            assembly_code = assembly_code.replace('SP','0')
            self.code.append(assembly_code)
            
            