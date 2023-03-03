import tweepy as tw
import pandas as pd
import time
import csv

cod_usuario = []
Nome = []
Localizacao = []
filtro_estado = []
Localizacao_real_Pais = []
Localizacao_real_Ciade = []
Dispo = []
Tweet = []
Seguidores = []
Cod_lin = []
Data = []
Curti = []


R_cod_usuario = []
R_original = []
R_Nome = []
R_Localizacao = []
R_filtro_estado = []
R_Localizacao_real_Pais = []
R_Localizacao_real_Ciade = []
R_Dispo = []
R_Tweet = []
R_Seguidores = []
R_Cod_lin = []
R_Data = []
R_Curti = []

# quantiodade de tweets

pegar = 30

quant = []

con = []
print('rodando')



def principal():

    consumer_key = "Wxr8vbYiHPkq0pCdo8klywAMV"
    consumer_secret = "Ms5Jiw9bqH61zrplIRnSNQUNuN5kTZoeCezW28ro3nG1DVg2qy"
    access_token = "318113208-7ArMDSMeoG42dtYXJCfmBqkk7bDJAGIc2oUZ2Zpv"
    access_token_secret = 'G34yrzl442QkgHO5nWOfxLiBzjFLO3Unx2PDjZkoVYe97'

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tw.API(auth)

    arquivo = 'gta'

    query_search = arquivo

    Qtweet = 100

    cursor_tweets = tw.Cursor(api.search, q=query_search).items(Qtweet)

    for tweet in cursor_tweets:
        print(tweet.text[0:4])

        try:
            original_tweeter_name = tweet.retweeted_status.user.screen_name
            Verifica = 'RT @'
            original_tweeter_id = tweet.retweeted_status.user.id
            original_tweet_id = tweet.retweeted_status.id
        except AttributeError:
            original_tweeter_name = None
            Verifica = 'None'
            original_tweeter_id = None
            original_tweet_id = None

        print(teste)



        # quantidade que já pegou
        con.append(tweet.user.name)
        if len(con) > 50:
            print('Tempo de 1 Min')
            time.sleep(60)
            con.clear()

        quant.append(tweet.user.name)


        # guardar
        if Verifica in tweet.text[0:4]:
            print("RT")
            # print("="*100)
            # print(tweet.user.screen_name, ' Retuitou de ', tweet.retweeted_status.user.screen_name)
            R_Data.append(tweet.created_at)  # Verificar depois
            R_cod_usuario.append(tweet.user.screen_name)
            R_original.append(tweet.retweeted_status.user.screen_name)
            R_Nome.append(tweet.user.name)

            if str(tweet.user.location) == "":
                R_Localizacao.append("Não Possui")
                R_filtro_estado.append("Não possui")
            else:
                R_Localizacao.append(str(tweet.user.location))
                if "Acre" in str(tweet.user.location).title() or " AC" in str(tweet.user.location) or "/AC" in str(
                        tweet.user.location) or ",AC" in str(tweet.user.location):
                    R_filtro_estado.append("Acre")

                elif "Alagoas" in str(tweet.user.location).title() or " AL" in str(tweet.user.location) or "/AL" in str(
                        tweet.user.location) or ",AL" in str(tweet.user.location):
                    R_filtro_estado.append("Alagoas")

                elif "Amapá" in str(tweet.user.location).title() or "Amapa" in str(
                        tweet.user.location).title() or " AP" in str(
                        tweet.user.location) or "/AP" in str(tweet.user.location) or ",AP" in str(tweet.user.location):
                    R_filtro_estado.append("Amapá")

                elif "Amazonas" in str(tweet.user.location).title() or " AM" in str(
                        tweet.user.location) or "/AM" in str(
                        tweet.user.location) or ",AM" in str(tweet.user.location):
                    R_filtro_estado.append("Amazonas")

                elif "Bahia" in str(tweet.user.location).title() or " BA" in str(tweet.user.location) or "/BA" in str(
                        tweet.user.location) or ",BA" in str(tweet.user.location):
                    R_filtro_estado.append("Bahia")

                elif "Ceará" in str(tweet.user.location).title() or "Ceara" in str(
                        tweet.user.location).title() or " CE" in str(
                        tweet.user.location) or "/CE" in str(tweet.user.location) or ",CE" in str(tweet.user.location):
                    R_filtro_estado.append("Ceará")

                elif "Distrito Federal" in str(tweet.user.location).title() or "Brasília" in str(
                        tweet.user.location) or "Brasilia" in str(tweet.user.location) or " DF" in str(
                    tweet.user.location) or "/DF" in str(tweet.user.location) or ",DF" in str(tweet.user.location):
                    R_filtro_estado.append("Distrito Federal")

                elif "Espírito Santo" in str(tweet.user.location).title() or " ES" in str(
                        tweet.user.location) or "/ES" in str(
                        tweet.user.location) or ",ES" in str(tweet.user.location):
                    R_filtro_estado.append("Espírito Santo")

                elif "Goiás" in str(tweet.user.location).title() or "Goias" in str(
                        tweet.user.location).title() or " GO" in str(
                        tweet.user.location) or "/GO" in str(tweet.user.location) or ",GO" in str(tweet.user.location):
                    R_filtro_estado.append("Goiás")

                elif "Maranhão" in str(tweet.user.location).title() or "Maranhao" in str(
                        tweet.user.location).title() or " MA" in str(
                    tweet.user.location) or "/MA" in str(tweet.user.location) or ",MA" in str(tweet.user.location):
                    R_filtro_estado.append("Maranhão")

                elif "Mato Grosso" in str(tweet.user.location).title() or " MT" in str(
                        tweet.user.location) or "/MT" in str(
                        tweet.user.location) or ",MT" in str(tweet.user.location):
                    R_filtro_estado.append("Mato Grosso")

                elif "Mato Grosso do Sul" in str(tweet.user.location) or " MS" in str(
                        tweet.user.location) or "/MS" in str(
                        tweet.user.location) or ",MS" in str(tweet.user.location):
                    R_filtro_estado.append("Mato Grosso do Sul")

                elif "Minas Gerais" in str(tweet.user.location).title() or " MG" in str(
                        tweet.user.location) or "/MG" in str(
                        tweet.user.location) or ",MG" in str(tweet.user.location):
                    R_filtro_estado.append("Minas Gerais")

                elif "Pará" in str(tweet.user.location).title() or " PA" in str(tweet.user.location) or "/PA" in str(
                        tweet.user.location) or ",PA" in str(tweet.user.location):
                    R_filtro_estado.append("Pará")

                elif "Paraíba" in str(tweet.user.location).title() or "Paraiba" in str(
                        tweet.user.location).title() or " PB" in str(
                    tweet.user.location) or "/PB" in str(tweet.user.location) or ",PB" in str(tweet.user.location):
                    R_filtro_estado.append("Paraíba")

                elif "Paraná" in str(tweet.user.location).title() or "Parana" in str(
                        tweet.user.location).title() or " PR" in str(
                    tweet.user.location) or "/PR" in str(tweet.user.location) or ",PR" in str(tweet.user.location):
                    R_filtro_estado.append("Paraná")

                elif "Pernambuco" in str(tweet.user.location).title() or " PE" in str(
                        tweet.user.location) or "/PE" in str(
                        tweet.user.location) or ",PE" in str(tweet.user.location):
                    R_filtro_estado.append("Pernambuco")

                elif "Piauí" in str(tweet.user.location).title() or "Piaui" in str(
                        tweet.user.location).title() or " PI" in str(
                        tweet.user.location) or "/PI" in str(tweet.user.location) or "PI" in str(tweet.user.location):
                    R_filtro_estado.append("Piauí")

                elif "rio de janeiro" in str(tweet.user.location).lower() or " RJ" in str(
                        tweet.user.location) or "/RJ" in str(
                        tweet.user.location) or ",RJ" in str(tweet.user.location):
                    R_filtro_estado.append("Rio de Janeiro")

                elif "rio grande do norte" in str(tweet.user.location).lower() or " RN" in str(
                        tweet.user.location) or "/RN" in str(
                    tweet.user.location) or ",RN" in str(tweet.user.location):
                    R_filtro_estado.append("Rio Grande do Norte")

                elif "rio grande do sul" in str(tweet.user.location).lower() or " RS" in str(
                        tweet.user.location) or "/RS" in str(
                    tweet.user.location) or ",RS" in str(tweet.user.location):
                    R_filtro_estado.append("Rio Grande do Sul")

                elif "Rondônia" in str(tweet.user.location).title() or "Rondonia" in str(
                        tweet.user.location).title() or " RO" in str(
                    tweet.user.location) or "/RO" in str(tweet.user.location) or ",RO" in str(tweet.user.location):
                    R_filtro_estado.append("Rondônia")

                elif "Roraima" in str(tweet.user.location).title() or "RR" in str(tweet.user.location):
                    R_filtro_estado.append("Roraima")

                elif "Santa Catarina" in str(tweet.user.location).title() or "SC" in str(tweet.user.location):
                    R_filtro_estado.append("Santa Catarina")

                elif "São Paulo" in str(tweet.user.location).title() or "Sao Paulo" in str(
                        tweet.user.location).title() or "SP" in str(
                    tweet.user.location):
                    R_filtro_estado.append("São Paulo")

                elif "Sergipe" in str(tweet.user.location).title() or "SE" in str(tweet.user.location):
                    R_filtro_estado.append("Sergipe")

                elif "Tocantins" in str(tweet.user.location).title() or "TO" in str(tweet.user.location):
                    R_filtro_estado.append("Tocantins")

                else:
                    #print("oie aqui")
                    R_filtro_estado.append("desconehcido")


            # localização real
            teste2 = str(tweet.place)

            if teste2 == 'None':
                # print('não')
                R_Localizacao_real_Pais.append("Não Possui")
                R_Localizacao_real_Ciade.append("Não Possui")
            else:
                # print(tweet.place)
                R_Localizacao_real_Pais.append(tweet.place.country)
                R_Localizacao_real_Ciade.append(tweet.place.name)

            R_Dispo.append(tweet.source)
            R_Tweet.append(tweet.text)
            R_Seguidores.append(tweet.user.followers_count)
            R_Cod_lin.append(tweet.lang)
            R_Curti.append(tweet.favorite_count)

        else:
            print("tweet")
            # print(tweet.user.screen_name)
            cod_usuario.append(tweet.user.screen_name)
            Data.append(tweet.created_at)
            # print(tweet.user.screen_name)
            # print(tweet._json)
            Nome.append(tweet.user.name)

            if str(tweet.user.location) == "":
                Localizacao.append("Não Possui")
                filtro_estado.append("Não possui")
            else:
                Localizacao.append(str(tweet.user.location))
                if "Acre" in str(tweet.user.location).title() or " AC" in str(tweet.user.location) or "/AC" in str(
                        tweet.user.location) or ",AC" in str(tweet.user.location):
                    filtro_estado.append("Acre")

                elif "Alagoas" in str(tweet.user.location).title() or " AL" in str(tweet.user.location) or "/AL" in str(
                        tweet.user.location) or ",AL" in str(tweet.user.location):
                    filtro_estado.append("Alagoas")

                elif "Amapá" in str(tweet.user.location).title() or "Amapa" in str(
                        tweet.user.location).title() or " AP" in str(
                        tweet.user.location) or "/AP" in str(tweet.user.location) or ",AP" in str(tweet.user.location):
                    filtro_estado.append("Amapá")

                elif "Amazonas" in str(tweet.user.location).title() or " AM" in str(
                        tweet.user.location) or "/AM" in str(
                        tweet.user.location) or ",AM" in str(tweet.user.location):
                    filtro_estado.append("Amazonas")

                elif "Bahia" in str(tweet.user.location).title() or " BA" in str(tweet.user.location) or "/BA" in str(
                        tweet.user.location) or ",BA" in str(tweet.user.location):
                    filtro_estado.append("Bahia")

                elif "Ceará" in str(tweet.user.location).title() or "Ceara" in str(
                        tweet.user.location).title() or " CE" in str(
                        tweet.user.location) or "/CE" in str(tweet.user.location) or ",CE" in str(tweet.user.location):
                    filtro_estado.append("Ceará")

                elif "Distrito Federal" in str(tweet.user.location).title() or "Brasília" in str(
                        tweet.user.location) or "Brasilia" in str(tweet.user.location) or " DF" in str(
                    tweet.user.location) or "/DF" in str(tweet.user.location) or ",DF" in str(tweet.user.location):
                    filtro_estado.append("Distrito Federal")

                elif "Espírito Santo" in str(tweet.user.location).title() or " ES" in str(
                        tweet.user.location) or "/ES" in str(
                        tweet.user.location) or ",ES" in str(tweet.user.location):
                    filtro_estado.append("Espírito Santo")

                elif "Goiás" in str(tweet.user.location).title() or "Goias" in str(
                        tweet.user.location).title() or " GO" in str(
                        tweet.user.location) or "/GO" in str(tweet.user.location) or ",GO" in str(tweet.user.location):
                    filtro_estado.append("Goiás")

                elif "Maranhão" in str(tweet.user.location).title() or "Maranhao" in str(
                        tweet.user.location).title() or " MA" in str(
                    tweet.user.location) or "/MA" in str(tweet.user.location) or ",MA" in str(tweet.user.location):
                    filtro_estado.append("Maranhão")

                elif "Mato Grosso" in str(tweet.user.location).title() or " MT" in str(
                        tweet.user.location) or "/MT" in str(
                        tweet.user.location) or ",MT" in str(tweet.user.location):
                    filtro_estado.append("Mato Grosso")

                elif "Mato Grosso do Sul" in str(tweet.user.location) or " MS" in str(
                        tweet.user.location) or "/MS" in str(
                        tweet.user.location) or ",MS" in str(tweet.user.location):
                    filtro_estado.append("Mato Grosso do Sul")

                elif "Minas Gerais" in str(tweet.user.location).title() or " MG" in str(
                        tweet.user.location) or "/MG" in str(
                        tweet.user.location) or ",MG" in str(tweet.user.location):
                    filtro_estado.append("Minas Gerais")

                elif "Pará" in str(tweet.user.location).title() or " PA" in str(tweet.user.location) or "/PA" in str(
                        tweet.user.location) or ",PA" in str(tweet.user.location):
                    filtro_estado.append("Pará")

                elif "Paraíba" in str(tweet.user.location).title() or "Paraiba" in str(
                        tweet.user.location).title() or " PB" in str(
                    tweet.user.location) or "/PB" in str(tweet.user.location) or ",PB" in str(tweet.user.location):
                    filtro_estado.append("Paraíba")

                elif "Paraná" in str(tweet.user.location).title() or "Parana" in str(
                        tweet.user.location).title() or " PR" in str(
                    tweet.user.location) or "/PR" in str(tweet.user.location) or ",PR" in str(tweet.user.location):
                    filtro_estado.append("Paraná")

                elif "Pernambuco" in str(tweet.user.location).title() or " PE" in str(
                        tweet.user.location) or "/PE" in str(
                        tweet.user.location) or ",PE" in str(tweet.user.location):
                    filtro_estado.append("Pernambuco")

                elif "Piauí" in str(tweet.user.location).title() or "Piaui" in str(
                        tweet.user.location).title() or " PI" in str(
                        tweet.user.location) or "/PI" in str(tweet.user.location) or "PI" in str(tweet.user.location):
                    filtro_estado.append("Piauí")

                elif "rio de janeiro" in str(tweet.user.location).lower() or " RJ" in str(
                        tweet.user.location) or "/RJ" in str(
                        tweet.user.location) or ",RJ" in str(tweet.user.location):
                    filtro_estado.append("Rio de Janeiro")

                elif "rio grande do norte" in str(tweet.user.location).lower() or " RN" in str(
                        tweet.user.location) or "/RN" in str(
                    tweet.user.location) or ",RN" in str(tweet.user.location):
                    filtro_estado.append("Rio Grande do Norte")

                elif "rio grande do sul" in str(tweet.user.location).lower() or " RS" in str(
                        tweet.user.location) or "/RS" in str(
                    tweet.user.location) or ",RS" in str(tweet.user.location):
                    filtro_estado.append("Rio Grande do Sul")

                elif "Rondônia" in str(tweet.user.location).title() or "Rondonia" in str(
                        tweet.user.location).title() or " RO" in str(
                    tweet.user.location) or "/RO" in str(tweet.user.location) or ",RO" in str(tweet.user.location):
                    filtro_estado.append("Rondônia")

                elif "Roraima" in str(tweet.user.location).title() or "RR" in str(tweet.user.location):
                    filtro_estado.append("Roraima")

                elif "Santa Catarina" in str(tweet.user.location).title() or "SC" in str(tweet.user.location):
                    filtro_estado.append("Santa Catarina")

                elif "São Paulo" in str(tweet.user.location).title() or "Sao Paulo" in str(
                        tweet.user.location).title() or "SP" in str(
                    tweet.user.location):
                    filtro_estado.append("São Paulo")

                elif "Sergipe" in str(tweet.user.location).title() or "SE" in str(tweet.user.location):
                    filtro_estado.append("Sergipe")

                elif "Tocantins" in str(tweet.user.location).title() or "TO" in str(tweet.user.location):
                    filtro_estado.append("Tocantins")

                else:
                    #print("oie aqui")
                    filtro_estado.append("desconehcido")



            Dispo.append(tweet.source)
            Tweet.append(tweet.text)
            Seguidores.append(tweet.user.followers_count)
            Cod_lin.append(tweet.lang)
            Curti.append(tweet.favorite_count)

            # localização Real
            teste = str(tweet.place)

            if teste == 'None':
                Localizacao_real_Pais.append("Não Possui")
                Localizacao_real_Ciade.append("Não Possui")
            else:
                Localizacao_real_Pais.append(tweet.place.country)
                Localizacao_real_Ciade.append(tweet.place.name)

        print(len(quant), 'de', Qtweet)



print(len(con))
principal()

while len(quant) < pegar:
    print(len(quant), 'de', pegar)
    print(pegar, 'aqui')
    if len(con) == 11:
        print(len(con), 'Quantos')
        print('tempo')
        time.sleep(5)
        con.clear()
    else:
        print('ok')
        print(len(quant))
        principal()


print(len(con))
print('='*100)
Normal = {

    "Data do post": Data,
    "@_Usuario": cod_usuario,
    "Nome da Conta": Nome,
    "Localização na conta": Localizacao,
    "Filtro_estado": filtro_estado,
    "País": Localizacao_real_Pais,
    "Cidade": Localizacao_real_Ciade,
    "Forma de Tweet": Dispo,
    "Tweet": Tweet,
    "Quantidade de Curtidas": Curti,
    "Quantidade de Seguidores": Seguidores,
    "Cod.Linguagem": Cod_lin}
df = pd.DataFrame(data=Normal)
print(df)

Retuite = {
    "Data do post": R_Data,
    "@_Usuario": R_cod_usuario,
    "@_original": R_original,
    "Nome da Conta": R_Nome,
    "Localização na conta": R_Localizacao,
    "Filtro_estado": R_filtro_estado,
    "País": R_Localizacao_real_Pais,
    "Cidade": R_Localizacao_real_Ciade,
    "Forma de Tweet": R_Dispo,
    "Tweet": R_Tweet,
    "Quantidade de Curtidas": R_Curti,
    "Quantidade de Seguidores": R_Seguidores,
    "Cod.Linguagem": R_Cod_lin}
frameR = pd.DataFrame(data=Retuite)
print(frameR)

nomesavalva = 'gta feminista'

df.to_csv(nomesavalva + ' ' + str(len(quant)) + ".csv")
frameR.to_csv(nomesavalva + 'Retuite' + ' ' + str(len(quant)) + '.csv')
