
export uniform int width() { return programCount; }


export void f_fu(uniform float RET[], uniform float aFOO[], uniform float b) {
    uniform int a[4][4][4];
    for (uniform int i = 0; i < 4; ++i)
        for (uniform int j = 0; j < 4; ++j)
            for (uniform int k = 0; k < 4; ++k)
                a[i][j][k] = 100*i+10*j+k;
    
    RET[programIndex] = *(a[2][3] + 1);
}

export void result(uniform float RET[]) {
    RET[programIndex] = 231;
}
