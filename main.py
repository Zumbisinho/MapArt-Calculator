import tkinter
primero_count = 0
primero_nome = 0
resultado = 0
resultado_total = 0
lista_final = {}
lista_output = {}
lista_output.clear()
lista_final.clear()
NAcount = 0
index = 0
resultado_desconto = 0
lines = []
# Troque os valores de acordo com o servidor! (Armamc.com Values)
valores_dos_blocos = {
    'Grass Block' : 6.25  ,
    'Slime Block' :  23.44,
    'Sand' :  4.69,
    'Sandstone' : 4.69 ,
    'Sandstone Slab' : 2 / 4.69 ,
    'Birch Log (vertical)' : 12.50 ,
    'Birch Planks' : 12.50 / 4 ,
    'Birch Slab' :  4 / 12.50 / 2,
    'Glowstone' :  25.00,
    'End Stone' :  7.03,
    'End Stone Bricks' : 7.81 ,
    'End Stone Brick Slab' : 2 / 7.81  ,
    'Bone Block' :  10.94,
    'Birch Pressure Plate' : 2 / 12.50 ,
    'Ochre Froglight' :  'N/A',
    'Cobweb' :  7.81,
    'Mushroom Stem' : 6.25 ,
    'White Candle' : 'N/A' ,
    'TNT' : 60.66 ,
    'Block of Redstone' :  70.31,
    'Ice' :  12.50,
    'Packed Ice' : 100 ,
    'Blue Ice' :  800,
    'Block of Iron' : 597.66 ,
    'Iron Trapdoor' :  66.41 * 4,
    'Weighted Pressure Plate (Heavy)' : 66.41 * 2 ,
    'Brewing Stand' :  6.25 * 5,
    'Leaves (Oak)' :  12.50,
    'Leaves (Spruce)' :  12.50,
    'Leaves (Birch)' :  12.50,
    'Leaves (Jungle)' :  12.50,
    'Leaves (Acacia)' :  12.50,
    'Leaves (Dark Oak)' :  12.50,
    'Leaves (Azalea)' :  'N/A',
    'Block of Bamboo (horizontal)' : 'N/A' ,
    'Clay' : 9.38 ,
    'Jungle Log (vertical)' : 12.50 ,
    'Jungle Planks' : 12.50 / 4 ,
    'Jungle Slab' :  12.50 / 8,
    'Dirt' :  4.69,
    'Coarse Dirt' : 6.25 ,
    'Rooted Dirt' :  4.69,
    'Jukebox' :  400,
    'Granite' :  6.25,
    'Granite Slab' : 6.25 /2  ,
    'Jungle Pressure Plate' :12.50 /2  ,
    'Packed Mud' :  'N/A',
    'Cobblestone' :  6.25,
    'Cobblestone Slab' : 6.25 /2,
    'Mossy Cobblestone' :  6.25 *2,
    'Mossy Cobblestone Slab' :  6.25,
    'Stone' :  7.81,
    'Stone Slab' : 7.81 /2 ,
    'Smooth Stone Slab' : 7.81 / 2 ,
    'Stone Bricks' :  7.81,
    'Stone Brick Slab' :  7.81 /2,
    'Andesite' :  6.25,
    'Andesite Slab' : 6.25 /2 ,
    'Bedrock' :  'N/A',
    'Acacia Log (horizontal)' : 12.50 ,
    'Gravel' :  4.69,
    'Stone Pressure Plate' : 6.25 /2 ,
    'Water (Unsupported!)' : 'N/A' ,
    'Oak Log (vertical)' : 12.50 ,
    'Oak Planks' :  12.50 /2,
    'Oak Slab' :  12.50 /8,
    'Crafting Table' :  12.50 ,
    'Oak Pressure Plate' :  12.50 /2,
    'Birch Log (horizontal)' :  12.50,
    'Diorite' :  6.25,
    'Diorite Slab' : 6.25 /2 ,
    'Quartz Block' :  25 ,
    'Quartz Slab' :  25 /2,
    'Sea Lantern' :  50,
    'White Wool' :  7.81,
    'White Carpet' :  7.81 * 1.5,
    'White Stained Glass' :  6.73,
    'White Concrete' :  4.69 + 0.48,
    'White Concrete Powder' :  4.69 + 0.48,
    'White Glazed Terracotta' :  7.81 + 0.48,
    'Snow Block' :  4.69,
    'Snow Layer' :  'N/A',
    'Orange Wool' :  7.81 + 3.91,
    'Orange Carpet' : 11.72 / 1.5 ,
    'Orange Stained Glass' :  6.73,
    'Orange Concrete' :  4.69 + 0.48,
    'Orange Concrete Powder' : 4.69 + 0.48 ,
    'Orange Glazed Terracotta' : 7.81 + 0.48 ,
    'Pumpkin' :  78.12,
    'Acacia Log (vertical)' : 12.50 ,
    'Acacia Planks' :  12.50 / 4,
    'Acacia Slab' :  12.50 / 8,
    'Red Sand' :  6.25,
    'Red Sandstone' :  6.25,
    'Red Sandstone Slab' : 6.25 /2 ,
    'Terracotta' :  7.81,
    'Honey Block' :  62.50,
    'Honeycomb Block' :  25.00,
    'Block Of Raw Copper' : 133.59 ,
    'Waxed Block Of Copper' :  'N/A',
    'Waxed Cut Copper Slab' :  'N/A',
    'Acacia Pressure Plate' :  12.50 /2,
    'Magenta Wool' :  7.81 + 3.81,
    'Magenta Carpet' : 11.72 /2,
    'Magenta Stained Glass' : 4.69 + 0.48 ,
    'Magenta Concrete' : 4.69 + 0.48 ,
    'Magenta Concrete Powder' :4.69 + 0.48  ,
    'Magenta Glazed Terracotta' : 4.69 + 0.48 ,
    'Purpur Block' : 7.81 ,
    'Purpur Slab' :  7.81 /2,
    'Light Blue Wool' :  11.72,
    'Light Blue Carpet' :  11.72 /2,
    'Light Blue Stained Glass' : 4.69 + 0.48 ,
    'Light Blue Concrete' : 4.69 + 0.48 ,
    'Light Blue Concrete Powder' : 4.69 + 0.48 ,
    'Light Blue Glazed Terracotta' : 4.69 + 0.48 ,
    'Yellow Wool' : 11.72 ,
    'Yellow Carpet' :  11.72 /2,
    'Yellow Stained Glass' : 4.69 + 0.48 ,
    'Yellow Concrete' : 4.69 + 0.48 ,
    'Yellow Concrete Powder' : 4.69 + 0.48 ,
    'Yellow Glazed Terracotta' : 4.69 + 0.48 ,
    'Hay Bale' : 93.75 ,
    'Sponge (any)' :  400.00,
    'Block of Bamboo (vertical)' : 'N/A' ,
    'Bamboo Planks' :  'N/A',
    'Bamboo Slab' :  'N/A',
    'Bamboo Mosaic' :  'N/A',
    'Bamboo Mosaic Slab' : 'N/A' ,
    'Bamboo Pressure Plate' :  'N/A',
    'Lime Wool' : 11.72 ,
    'Lime Carpet' : 11.72 /2 ,
    'Lime Stained Glass' : 4.69 + 0.48 ,
    'Lime Concrete' : 4.69 + 0.48 ,
    'Lime Concrete Powder' : 4.69 + 0.48 ,
    'Lime Glazed Terracotta' : 4.69 + 0.48 ,
    'Melon' : 78.12 ,
    'Pink Wool' : 11.72 ,
    'Pink Carpet' : 11.72 /2 ,
    'Pink Stained Glass' : 4.69 + 0.48 ,
    'Pink Concrete' : 4.69 + 0.48 ,
    'Pink Concrete Powder' : 4.69 + 0.48 ,
    'Pink Glazed Terracotta' : 4.69 + 0.48 ,
    'Pearlescent Froglight' : 'N/A' ,
    'Cherry Leaves' : 'N/A' ,
    'Gray Wool' : 11.72 ,
    'Gray Carpet' : 11.72 /2 ,
    'Gray Stained Glass' : 4.69 + 0.48 ,
    'Gray Concrete' : 4.69 + 0.48 ,
    'Gray Concrete Powder' : 4.69 + 0.48 ,
    'Gray Glazed Terracotta' : 4.69 + 0.48 ,
    'Dead Tube Coral Block' : 'N/A' ,
    'Dead Brain Coral Block' : 'N/A' ,
    'Dead Bubble Coral Block' :  'N/A',
    'Dead Fire Coral Block' : 'N/A' ,
    'Dead Horn Coral Block' :  'N/A',
    'Tinted Glass' : 'N/A' ,
    'Light Gray Wool' : 11.72 ,
    'Light Gray Carpet' : 11.72 /2 ,
    'Light Gray Stained Glass' : 4.69 + 0.48 ,
    'Light Gray Concrete' : 4.69 + 0.48 ,
    'Light Gray Concrete Powder' : 4.69 + 0.48 ,
    'Light Gray Glazed Terracotta' : 4.69 + 0.48 ,
    'Cyan Wool' : 11.72 ,
    'Cyan Carpet' : 11.72 /2 ,
    'Cyan Stained Glass' : 4.69 + 0.48 ,
    'Cyan Concrete' : 4.69 + 0.48 ,
    'Cyan Concrete Powder' : 4.69 + 0.48 ,
    'Cyan Glazed Terracotta' : 4.69 + 0.48 ,
    'Prismarine' : 10.94 ,
    'Prismarine Slab' : 10.94 /2 ,
    'Purple Wool' : 11.72 ,
    'Purple Carpet' : 11.72 /2 ,
    'Purple Stained Glass' : 4.69 + 0.48 ,
    'Purple Concrete' : 4.69 + 0.48 ,
    'Purple Concrete Powder' : 4.69 + 0.48 ,
    'Purple Glazed Terracotta' : 4.69 + 0.48 ,
    'Mycelium' : 10.94 ,
    'Amethyst Block' : 'N/A' ,
    'Blue Wool' : 11.72 ,
    'Blue Carpet' : 11.72 /2 ,
    'Blue Stained Glass' :4.69 + 0.48  ,
    'Blue Concrete' : 4.69 + 0.48 ,
    'Blue Concrete Powder' : 4.69 + 0.48 ,
    'Blue Glazed Terracotta' : 4.69 + 0.48 ,
    'Brown Wool' : 11.72 ,
    'Brown Carpet' : 11.72 /2 ,
    'Brown Stained Glass' : 4.69 + 0.48 ,
    'Brown Concrete' : 4.69 + 0.48 ,
    'Brown Concrete Powder' : 4.69 + 0.48 ,
    'Brown Glazed Terracotta' : 4.69 + 0.48 ,
    'Dark Oak Log (any direction)' : 12.50 ,
    'Dark Oak Planks' : 12.50 /4 ,
    'Dark Oak Slab' : 12.50 /8 ,
    'Spruce Log (horizontal)' : 12.50 ,
    'Soul Sand' : 4.69 ,
    'Soul Soil' : 'N/A' ,
    'Dark Oak Pressure Plate' : 12.50 /2 ,
    'Green Wool' : 11.72 ,
    'Green Carpet' : 11.72 /2 ,
    'Green Stained Glass' : 4.69 + 0.48 ,
    'Green Concrete' : 4.69 + 0.48 ,
    'Green Concrete Powder' : 4.69 + 0.48 ,
    'Green Glazed Terracotta' : 4.69 + 0.48 ,
    'Dried Kelp Block' : 'N/A' ,
    'Red Wool' : 11.72 ,
    'Red Carpet' : 11.72 /2 ,
    'Red Stained Glass' : 4.69 + 0.48 ,
    'Red Concrete' : 4.69 + 0.48 ,
    'Red Concrete Powder' : 4.69 + 0.48 ,
    'Red Glazed Terracotta' : 4.69 + 0.48 ,
    'Bricks' : 25.00 ,
    'Bricks Slab' : 25.00 /2 ,
    'Nether Wart Block' : 7.81 ,
    'Shroomlight' : 25.00 ,
    'Mangrove Log (vertical)' : 'N/A' ,
    'Mangrove Planks' : 'N/A' ,
    'Mangrove Slab' : 'N/A' ,
    'Mangrove Pressure Plate' : 'N/A' ,
    'Black Wool' : 11.72 ,
    'Black Carpet' : 11.72 /2 ,
    'Black Stained Glass' : 4.69 + 0.48 ,
    'Black Concrete' : 4.69 + 0.48 ,
    'Black Concrete Powder' : 4.69 + 0.48 ,
    'Black Glazed Terracotta' : 4.69 + 0.48 ,
    'Block of Coal' : 84.38 ,
    'Obsidian' : 28.12 ,
    'Crying Obsidian' : 31.25 ,
    'Blackstone' : 9.38 ,
    'Blackstone Slab' : 9.38 /2 ,
    'Basalt' : 9.38 ,
    'Block Of Netherite' : 'N/A' ,
    'Polished Blackstone Pressure Plate' : 9.28 * 2 ,
    'Sculk' : 'N/A' ,
    'Sculk Catalyst' : 'N/A' ,
    'Sculk Shrieker' : 'N/A' ,
    'Block of Gold' : 546.88 ,
    'Weighted Pressure Plate (Light)' : 60.16 ,
    'Block Of Raw Gold' : 492.19 ,
    'Block of Diamond' : 3375.00 ,
    'Prismarine Bricks' :  14.06,
    'Prismarine Brick Slab' : 14.06 /8 ,
    'Dark Prismarine' :  14.06,
    'Dark Prismarine Slab' : 14.06 /8 ,
    'Beacon' :  'N/A',
    'Lapis Lazuli Block' : 70.31 ,
    'Block of Emerald' :  562.00,
    'Spruce Log (vertical)' : 12.50 ,
    'Spruce Planks' : 12.50 /4 ,
    'Spruce Slab' : 12.50 /8 ,
    'Oak Log (horizontal)' : 12.50 ,
    'Jungle Log (horizontal)' : 12.50 ,
    'Podzol' : 9.38 ,
    'Spruce Pressure Plate' : 12.50 /2 ,
    'Mangrove Log (horizontal)' : 'N/A' ,
    'Mangrove Roots' : 'N/A' ,
    'Netherrack' : 3.12 ,
    'Nether Brick' : 9.38 ,
    'Nether Brick Slab' : 9.38 /2 ,
    'Magma Block' : 3.12 ,
    'Red Nether Bricks' : 10.94 ,
    'Red Nether Brick Slab' : 10.94 /2 ,
    'White Terracotta' : 7.81 + 0.48 ,
    'Calcite' : 6.25 ,
    'Cherry Planks' : 'N/A' ,
    'Cherry Slab' : 'N/A' ,
    'Cherry Log (vertical)' : 'N/A' ,
    'Stripped Cherry Log (vertical)' : 'N/A' ,
    'Cherry Pressure Plate' : 'N/A' ,
    'Orange Terracotta' : 7.81 + 0.48 ,
    'Magenta Terracotta' : 7.81 + 0.48 ,
    'Light Blue Terracotta' : 7.81 + 0.48 ,
    'Yellow Terracotta' : 7.81 + 0.48 ,
    'Lime Terracotta' : 7.81 + 0.48 ,
    'Pink Terracotta' : 7.81 + 0.48 ,
    'Stripped Cherry Log (horizontal)' : 'N/A' ,
    'Stripped Cherry Wood' : 'N/A' ,
    'Gray Terracotta' : 7.81 + 0.48 ,
    'Tuff' : 6.25 ,
    'Cherry Log (horizontal)' : 'N/A' ,
    'Cherry Wood' : 'N/A' ,
    'Light Gray Terracotta' : 7.81 + 0.48 ,
    'Waxed Exposed Copper' : 'N/A' ,
    'Waxed Exposed Cut Copper Slab' : 'N/A' ,
    'Mud Bricks' : 'N/A' ,
    'Mud Brick Slab' : 'N/A' ,
    'Cyan Terracotta' : 7.81 + 0.48 ,
    'Mud' : 'N/A' ,
    'Purple Terracotta' : 7.81 + 0.48 ,
    'Blue Terracotta' : 7.81 + 0.48 ,
    'Brown Terracotta' : 7.81 + 0.48 ,
    'Dripstone Block' : 7.81 + 0.48 ,
    'Pointed Dripstone' : 7.81 + 0.48 ,
    'Green Terracotta' : 7.81 + 0.48 ,
    'Red Terracotta' : 7.81 + 0.48 ,
    'Black Terracotta' : 7.81 + 0.48 ,
    'Crimson Nylium' : 6.25 ,
    'Crimson Stem' : 12.50 ,
    'Stripped Crimson Stem' : 12.50 ,
    'Crimson Planks' : 12.50 /4 ,
    'Crimson Slab' : 12.50 /8 ,
    'Crimson Pressure Plate' :12.50 /2  ,
    'Crimson Hyphae' : 12.50 ,
    'Stripped Crimson Hyphae' : 12.50 ,
    'Warped Nylium' : 6.25 ,
    'Waxed Oxidized Copper' : 'N/A' ,
    'Waxed Oxidized Cut Copper Slab' : 'N/A' ,
    'Warped Stem' : 12.50 ,
    'Stripped Warped Stem' : 12.50 ,
    'Warped Planks' : 12.50 /4 ,
    'Warped Slab' : 12.50 /8 ,
    'Waxed Weathered Copper' : 'N/A' ,
    'Waxed Weathered Cut Copper Slab' : 'N/A' ,
    'Warped Pressure Plate' : 12.50 /2 ,
    'Warped Hyphae' : 12.50 ,
    'Stripped Warped Hyphae' : 12.50 ,
    'Warped Wart Block' : 7.81 ,
    'Deepslate' : 9.38 ,
    'Cobbled Deepslate' : 6.25 ,
    'Cobbled Deepslate Slab' : 6.25 /2 ,
    'Block Of Raw Iron' : 428.91 ,
    'Glow Lichen' : 'N/A' ,
    'Verdant Froglight' : 'N/A'
}

janela = tkinter.Tk()
janela.geometry('1000x800')
janela.title('Calculador de Maparts!')

rotulo = tkinter.Label(janela,text=('Digite sua lista aqui!'),font=('Arial',20))
rotulo.grid(row=1,column=1)

rotulo_result = tkinter.Label(janela,text=('Resultado:'),font=('Arial',20))
rotulo_result.grid(row=1,column=3,padx=133)

saida = tkinter.Label(janela,text=(''),width=33,height=28,bd=3,relief='groove',justify='left',anchor='nw',font=('Arial',15))
saida.grid(row=2,column=3)

ajuda = tkinter.Label(janela,text='Leia o README.md\nAntes de utilizar\n A ferramenta!\n🤠',font=('Arial',15))
ajuda.grid(row=2,column=2,padx=10)

rotulo_total_result = tkinter.Label(janela,text='Resultado Total:',font=('Arial',10))
rotulo_total_result.grid(row=3,column=3)

saida_total = tkinter.Label(janela,text=(''),width=25,height=1,bd=2,relief='groove',font=('Arial',10,'bold'))
saida_total.grid(row=4,column=3)

entrada = tkinter.Text(janela, width=45,height=40,bd=3,relief='groove')
entrada.grid(row=2,column=1,padx=15)

desconto_label = tkinter.Label(janela,text=('Digite o desconto:'),font=('Arial',10))
desconto_label.grid(row=3,column=1)

valor_padrao = tkinter.StringVar()
valor_padrao.set(0)

desconto_text = tkinter.Entry(janela,relief='groove',textvariable=valor_padrao,bd=2)
desconto_text.grid(row=4,column=1)

def calcularvalor(count, nome):
    global resultado
    global NAcount
    if nome == 'reset':
        NAcount = 0
    else:
        if nome in valores_dos_blocos:
            if valores_dos_blocos[nome] != 'N/A':
                resultado = int(valores_dos_blocos[nome]) * int(count[0])
            else:
                NAcount = NAcount + 1
                resultado = 'N/A'
        return resultado, NAcount
        


def getlines():
    global resultado_total
    linhas = (entrada.get("1.0",tkinter.END)).splitlines()
    desconto = (desconto_text.get())
    global index
    nome = ''
    count = ''
    for line in linhas:
        index = index + 1
        if index == 1 or index == 2:
            print('ignorando')
        else:
            if not index % 2 == 0:
                nome = line
            else:
                    count = str(line).split(' ')
                    calc = calcularvalor(count,nome)
                    nacalc = calc[1]
                    result = calc[0]
                    if nome in lista_final:
                        if result != 'N/A':
                            lista_final[nome] = int(lista_final.get(nome)) + int(result*int(desconto)/100)
                        else:
                            lista_final[nome] = result
                    else:
                        if result != 'N/A':
                            lista_final[nome]= int(result - int(result*(int(desconto)/100)))
                        else:
                            lista_final[nome] = result

    values = lista_final.values()
    for valor in values:
        if valor != 'N/A':
            resultado_total = resultado_total + valor
    if resultado_total > 1000000:
        x = '%.1f'%float(resultado_total / 1000000)
        resultado_total = f'{x}M'
    elif resultado_total > 1000:
        x = '%.1f'%float(resultado_total / 1000)
        resultado_total = f'{x}K'

    for n,v in lista_final.items():
        #lista_output = valor.simplificado
        if v != 'N/A': #Number
            if v > 1000000:
                x = '%.1f'%float(v / 1000000)
                lista_output[n] = f'{x}M'
            elif v > 1000:
                x = '%.1f'%float(v / 1000)
                lista_output[n]= f'{x}K'
            else:
                lista_output[n] = v
        else:
            lista_output[n] = v

    lista_string = '\n'.join(f'{k}: {v}'for k,v in lista_output.items())
    saida.config(text=lista_string)
    saida_total.config(text=f'{resultado_total} Coins e {nacalc} Sem Valor!')
    calcularvalor(1,'reset')
    calc = ''
    resultado = 0
    resultado_total = 0
    lista_final.clear()
    lista_output.clear()
    nacalc = 0
    index = 0
    lines = []
    nome = ''
    count = ''
    calculo = 0

botao = tkinter.Button(janela,text='Calcular!',font=20,command=getlines)
botao.grid(row=5,column=1)

janela.mainloop()
