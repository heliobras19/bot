import wget
import requests

url = "http://23.111.155.130:1671/PainelAdministrador/PG_Registros/Pg.ExportarDados.php?CodigoImportacao1=&CodigoBioma=0&EndEstado2=MS&EndCidade2=Aquidauana&CodigoStatusImovel=0&CodigoTipoImovel=0&CodigoSituacao=0&CodigoCondicao=0&CodigoCondicaoPRA=0&CodigoSituacaoRL=0&HouveRetificacao=0&AderiuPRA=0&IsChecado=0&DataRegistroDe=&DataRegistroAte=&DataRetificacaoDe=&DataRetificacaoAte=&ModuloFiscalDe=4&ModuloFiscalAte=&SaldoReservaLegalDe=&SaldoReservaLegalAte=&ExBusca=S"
myfile = requests.get(url, allow_redirects=True)

output = open('teste.xls', 'wb')
output.write(myfile.content)
output.close()

cidades = ['Alcin%C3%B3polis','Amambai','Anast%C3%A1cio','Anauril%C3%A2ndia','Ang%C3%A9lica','Ant%C3%B4nio+Jo%C3%A3o','Aparecida+do+Taboado','Aquidauana','Aral+Moreira','%C3%81gua+Clara','Bandeirantes','Bataguassu','Bataypor%C3%A3','Bela+Vista','Bodoquena','Bonito','Brasil%C3%A2ndia','Caarap%C3%B3','Camapu%C3%A3','Campo+Grande','Caracol','Cassil%C3%A2ndia','Chapad%C3%A3o+do+Sul','Corguinho','Coronel+Sapucaia','Corumb%C3%A1','Costa+Rica','Coxim','Deod%C3%A1polis','Dois+Irm%C3%A3os+do+Buriti','Douradina','Dourados','Eldorado','F%C3%A1tima+do+Sul','Figueir%C3%A3o','Gl%C3%B3ria+de+Dourados','Guia+Lopes+da+Laguna','Iguatemi','Inoc%C3%AAncia','Itapor%C3%A3','Itaquira%C3%AD','Ivinhema','Japor%C3%A3','Jaraguari','Jardim','Jate%C3%AD','Juti','Lad%C3%A1rio','Laguna+Carap%C3%A3','Maracaju','Miranda','Mundo+Novo','Navira%C3%AD','Nioaque','Nova+Alvorada+do+Sul','Nova+Andradina','Novo+Horizonte+do+Sul','Para%C3%ADso+das+%C3%81guas','Parana%C3%ADba','Paranhos','Pedro+Gomes','Ponta+Por%C3%A3','Porto+Murtinho','Ribas+do+Rio+Pardo','Rio+Brilhante','Rio+Negro','Rio+Verde+de+Mato+Grosso','Rochedo','Santa+Rita+do+Pardo','S%C3%A3o+Gabriel+do+Oeste','Selv%C3%ADria','Sete+Quedas','Sidrol%C3%A2ndia','Sonora','Tacuru','Taquarussu','Terenos','Tr%C3%AAs+Lagoas','Vicentina']
