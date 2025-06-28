map = {
    "push segment i": "@segmentPointer \nD=M \n@i \nD=D+A \n@addr \nM=D \nA=M \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n",
    "pop segment i": "@segmentPointer \nD=M \n@i \nD=D+A \n@addr \nM=D \n@SP \nM=M-1 \n@SP \nA=M \nD=M \n@addr \nA=M \nM=D \n",

    "push constant i": "@i \nD=A \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n",

    "pop static i": "@SP \nAM=M-1 \nD=M \n@Foo.i \nM=D \n",
    "push static i": "@Foo.i \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n",

    "push temp i": "@5 \nD=A \n@i \nD=D+A \n@addr \nM=D \nA=M \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n",
    "pop temp i": "@5 \nD=A \n@i \nD=D+A \n@addr \nM=D \n@SP \nM=M-1 \n@SP \nA=M \nD=M \n@addr \nA=M \nM=D \n",

    "push pointer 0": "@THIS \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n",
    "push pointer 1": "@THAT \nD=M \n@SP \nA=M \nM=D \n@SP \nM=M+1 \n",
    "pop pointer 0": "@SP \nM=M-1 \n@SP \nA=M \nD=M \n@THIS \nM=D \n",
    "pop pointer 1": "@SP \nM=M-1 \n@SP \nA=M \nD=M \n@THAT \nM=D \n",

    # 算术指令
    "add": "@SP \nAM=M-1 \nD=M \nA=A-1 \nM=M+D \n",
    "sub": "@SP \nAM=M-1 \nD=M \nA=A-1 \nM=M-D \n",
    "and": "@SP \nAM=M-1 \nD=M \nA=A-1 \nM=D&M \n",
    "or": "@SP \nAM=M-1 \nD=M \nA=A-1 \nM=D|M \n",
    
    # 单操作数指令
    "neg": "@SP \nA=M-1 \nM=-M \n",
    "not": "@SP \nA=M-1 \nM=!M \n",
    
    # 比较指令（需唯一标签）
    "eq": 
        "@SP \nAM=M-1 \nD=M \n@SP \nA=M-1 \nD=M-D \n@EQ_TRUE_{} \nD;JEQ \n@SP \nA=M-1 \nM=0 \n@EQ_END_{} \n0;JMP \n(EQ_TRUE_{}) \n@SP \nA=M-1 \nM=-1 \n(EQ_END_{}) \n"
    ,
    "gt": 
        "@SP \nAM=M-1 \nD=M \n@SP \nA=M-1 \nD=M-D \n@GT_TRUE_{} \nD;JGT \n@SP \nA=M-1 \nM=0 \n@GT_END_{} \n0;JMP \n(GT_TRUE_{}) \n@SP \nA=M-1 \nM=-1 \n(GT_END_{}) \n"
    ,
    "lt": 
        "@SP \nAM=M-1 \nD=M \n@SP \nA=M-1 \nD=M-D \n@LT_TRUE_{} \nD;JLT \n@SP \nA=M-1 \nM=0 \n@LT_END_{} \n0;JMP \n(LT_TRUE_{}) \n@SP \nA=M-1 \nM=-1 \n(LT_END_{}) \n"
    ,
}


