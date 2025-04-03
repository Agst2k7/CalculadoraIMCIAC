import pygame
import os
import flet as ft
pygame.mixer.init()



def saudavel():
        somc = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'correct.mp3'))
        somc.set_volume(1)
        somc.play()

def main(page: ft.Page):
    page.bgcolor=ft.colors.WHITE
    icone_path = os.path.join(os.path.dirname(__file__), 'golden_apple.ico')
    page.title = 'Calculadora IMC / IAC by Augusto'
    page.window_icon = icone_path  


    def toggle_fields(e):
          if tipo.value == "IAC":
            circunferencia.visible = True
            peso.visible = False
          else:
            circunferencia.visible = False
            peso.visible = True
          page.update()

    def calc(e): 
        if tipo.value=='IMC':
                if peso.value == '' or altura.value == '' or genero.value == '':
                    page.banner.open = True
                    page.update()
                else:
                    if ',' in altura.value:
                          altura.value = altura.value.replace(',', '.')
                    v_peso = float(peso.value)
                    v_altura = float(altura.value)

                    # Calcular IMC
                    imc = v_peso / (v_altura**2)
                    imc = round(imc, 2)

                    
                    IMC.value = f'Seu IMC é {imc:.2f}'

                    
                    
                    if imc < 18.5:
                            img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                            detalhes.value = 'Abaixo do peso'
                            detalhes.color = ft.colors.PURPLE
                            texto_aviso.value='Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.'
                    elif 18.5 <= imc < 24.9:
                            saudavel()
                            img_result.src = (os.path.join(os.path.dirname(__file__), 'good.png'))
                            detalhes.value = 'Peso saudável!'
                            detalhes.color = ft.colors.GREEN
                            texto_aviso.value='Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.'
                    elif 25 <= imc < 29.9:
                            img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                            detalhes.value = 'Sobrepeso'
                            detalhes.color = ft.colors.LIME_ACCENT_100
                            texto_aviso.value='O sobrepeso é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer.'
                    elif 30 <= imc < 34.9:
                            img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                            detalhes.value = 'Obesidade Grau 1'
                            detalhes.color = ft.colors.ORANGE
                            texto_aviso.value='Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.'
                    else:
                            img_result.src = (os.path.join(os.path.dirname(__file__), 'bruh.png'))   
                            detalhes.value = 'Obesidade Grave'
                            detalhes.color = ft.colors.RED
                            texto_aviso.value='Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.'
        else:
            
                if circunferencia.value == '' or altura.value == '' or genero.value == '':
                    page.banner.open = True
                    page.update()
                else:
                      if ',' in altura.value:
                          altura.value = altura.value.replace(',', '.')
                      v_altura = float(altura.value)
                      v_c_quadril = float(circunferencia.value)

                      #calc IAC
                      iac = (v_c_quadril/(v_altura**1.5)) - 18
                      IMC.value = f'Seu IAC é {iac:.2f}'

                      if genero.value == 'Feminino':

                        if iac < 16.9:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                                detalhes.value = 'Extremamente abaixo do peso!'
                                detalhes.color = ft.colors.RED
                                texto_aviso.value='Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.'
                        if 17 <= iac <20.9:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                                detalhes.value = 'Abaixo do peso'
                                detalhes.color = ft.colors.PURPLE
                                texto_aviso.value='Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.'
                        if 21 <= iac <32.9:
                                saudavel()
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'good.png'))
                                detalhes.value = 'Peso saudável!'
                                detalhes.color = ft.colors.GREEN
                                texto_aviso.value='Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.'
                        if 33 <= iac<38.9:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                                detalhes.value = 'Sobrepeso'
                                detalhes.color = ft.colors.LIME_ACCENT_100
                                texto_aviso.value='Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.'
                        if iac > 39:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'bruh.png'))
                                detalhes.value = 'Obesidade Grave'
                                detalhes.color = ft.colors.RED
                                texto_aviso.value='Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.'
                      else:
                        if iac < 4.99:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                                detalhes.value = 'Extremamente abaixo do peso!'
                                detalhes.color = ft.colors.RED
                                texto_aviso.value='Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.'
                        if 5<=iac < 7.9:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                                detalhes.value = 'Abaixo do peso'
                                detalhes.color = ft.colors.PURPLE
                                texto_aviso.value='Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.'
                        if 8 <= iac <20.9:
                                saudavel()
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'good.png'))
                                detalhes.value = 'Peso saudável!'
                                detalhes.color = ft.colors.GREEN
                                texto_aviso.value = 'Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.'
                        if 21 <= iac<25.9:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'danger.png'))
                                detalhes.value = 'Sobrepeso'
                                detalhes.color = ft.colors.LIME_ACCENT_100
                                texto_aviso.value = 'Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.'
                        if iac > 26:
                                img_result.src = (os.path.join(os.path.dirname(__file__), 'bruh.png'))
                                detalhes.value = 'Obesidade Grave'
                                detalhes.color = ft.colors.RED
                                texto_aviso.value = 'Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.'
                            
                            
                        
                 
        texto_aviso.update()   
        IMC.update()
        detalhes.update()
        img_result.update()
        page.update()

    def close_banner(e):
        page.banner.open = False
        page.update()

    # page cfg
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text('Calculadora IMC / IAC by agst'),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT
    )

    page.window_width = 400
    page.window_height = 550

    # Banner de erro
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text('Ops, Preencha todos os campos.'),
        actions=[
            ft.TextButton('OK', on_click=close_banner),
        ],
    )
    page.add(page.banner)

    # Campos de entrada
    tipo = ft.Dropdown(
          label='Tipo',
          hint_text='Escolha o tipo de calculadora',
          options=[
                ft.DropdownOption('IMC'),
                ft.DropdownOption('IAC')
          ],
          on_change=toggle_fields,
          
    )
    #dados
    altura = ft.TextField(label='Altura (m)', hint_text='Ex: 1.75')
    peso = ft.TextField(label='Peso (kg)', hint_text='Ex: 70')
    circunferencia = ft.TextField(label='Circunferência do quadril (cm)')
    genero = ft.Dropdown(
        label='Gênero',
        hint_text='Escolha seu gênero',
        options=[
            ft.dropdown.Option('Masculino'),
            ft.dropdown.Option('Feminino'),
        ]
    )

    # Botao calcular
    b_calcular = ft.ElevatedButton(text='Calcular IMC',width=150, height=75,on_click=calc, style=ft.ButtonStyle(
          shape=ft.RoundedRectangleBorder(radius=10),
          bgcolor=ft.colors.BLUE,
          color=ft.colors.WHITE
    ))

    # Imagem resultado
    img_result = ft.Image(
        src= (os.path.join(os.path.dirname(__file__), 'capa.png')), 
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    # inf result
    IMC = ft.Text(f'Seu IMC/IAC é ...', size=45)
    detalhes = ft.Text('Insira seus dados', size=35)

    texto_aviso = ft.Text('',size=20)

    info_app_resultado = ft.Column(
        controls=[
            IMC,
            detalhes,
        ]
    )

    info = ft.Row(
        controls=[
            info_app_resultado,
            img_result,
        ]
    )

    # Layout principal
    layoutimc = ft.Column(
        [
            ft.Container(
                info,
                padding=5,
                alignment=ft.alignment.center,
            ),

            ft.Container(
                tipo,
                padding=5,
                bgcolor=ft.colors.WHITE,
            ),

            ft.Container(
                peso,
                padding=5,
                bgcolor=ft.colors.WHITE,
            ),
            ft.Container(
                altura,
                padding=5,  
                bgcolor=ft.colors.WHITE,
            ),

            ft.Container(
                circunferencia,
                padding=5,
                bgcolor=ft.colors.WHITE,
            ),

            ft.Container(
                genero,
                padding=5,
                bgcolor=ft.colors.WHITE,
            ),
            ft.Container(
                b_calcular,
                padding=5,
                bgcolor=ft.colors.WHITE,
                alignment=ft.alignment.center
            ),
            ft.Container(
                texto_aviso,
                padding=5,
                bgcolor=ft.colors.WHITE,
            ),
        ]
    )

    page.add(layoutimc)
    

ft.app(target=main)
