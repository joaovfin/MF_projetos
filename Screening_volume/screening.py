#Importando bibliotecas
import time
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
from matplotlib import pyplot as plt
from datetime import datetime, timedelta


def ask_choice(initial_text, inquire_text, options: list[str]) -> str:
    """
    Função que solicita ao usuário que escolha um item de uma lista.
    """
    print(initial_text)

    for i, x in enumerate(options):
        print("  {} - {}".format(i+1, x))

    print()  # Cria linha vazia para harmonizar texto

    while True:
        choice = input(inquire_text)

        if not choice.isnumeric():
            print("Digite uma opção válida.")
        elif int(choice) not in list(range(len(options)+1)[1:]):
            print("Digite uma opção válida.")
        else:
            return options[int(choice)-1]

# Função que ajusta nome dos ativos, tira o .SA
def fix_col_names(df):
  return ['IBOV' if col == '^BVSP' else col.rstrip('.SA') for col in df.columns]


tickers = ['Ações BR', 'Cripto', 'FIIs', 'ETF-US', 'ETF-BR', 'Commodities', 'Ações US' ]
ticker = ask_choice("Opções disponíveis:", "Escolha uma opção: ", tickers)

acoes = ['AMER3.SA', 'RENT3.SA', 'HAPV3.SA',	'COGN3.SA',	'ITUB4.SA',	'BBDC4.SA',	'VALE3.SA',	'IFCM3.SA',	'B3SA3.SA',	'PETR4.SA',	'AZUL4.SA',	'ITSA4.SA',	'CIEL3.SA',	'RAIZ4.SA',	'CMIG4.SA',	'MGLU3.SA',	'MLAS3.SA',	'JBSS3.SA',	'ABEV3.SA',	'RDOR3.SA',	'BBAS3.SA',	'ENEV3.SA',	'LREN3.SA',	'MRVE3.SA',	'CMIN3.SA',	'LWSA3.SA',	'CPLE6.SA',	'NTCO3.SA',	'ONCO3.SA',	'USIM5.SA',	'RAIL3.SA',	'PCAR3.SA',	'CVCB3.SA',	'BRFS3.SA',	'ASAI3.SA',	'RADL3.SA',	'BEEF3.SA',	'PETR3.SA',	'ANIM3.SA',	'GGBR4.SA',	'CSAN3.SA',	'PETZ3.SA',	'CSNA3.SA',	'PRIO3.SA',	'EQTL3.SA',	'TIMS3.SA',	'ALPA4.SA',	'BBDC3.SA',	'WEGE3.SA',	'MRFG3.SA',	'VVEO3.SA',	'VAMO3.SA',	'POMO4.SA',	'MOVI3.SA',	'GOAU4.SA',	'VBBR3.SA',	'ELET3.SA',	'SUZB3.SA',	'ALOS3.SA',	'LJQQ3.SA',	'CRFB3.SA',	'STBP3.SA',	'RRRP3.SA',	'UGPA3.SA',	'EMBR3.SA',	'MULT3.SA',	'BBSE3.SA',	'AURE3.SA',	'VIVA3.SA',	'BHIA3.SA',	'CCRO3.SA',	'CPLE3.SA',	'JFEN3.SA',	'SEQL3.SA',	'TRPL4.SA',	'SBSP3.SA',	'HYPE3.SA',	'YDUQ3.SA',	'CLSA3.SA',	'AZEV4.SA',	'GFSA3.SA',	'SMFT3.SA',	'SIMH3.SA',	'PDGR3.SA',	'TEND3.SA',	'FLRY3.SA',	'BRAP4.SA',	'CYRE3.SA',	'TOTS3.SA',	'CBAV3.SA',	'SRNA3.SA',	'JHSF3.SA',	'ENJU3.SA',	'SLCE3.SA',	'CEAB3.SA',	'HBSA3.SA',	'GOLL4.SA',	'BRSR6.SA',	'POSI3.SA',	'VIVT3.SA',	'ECOR3.SA',	'AZZA3.SA',	'BRKM5.SA',	'QUAL3.SA',	'AESB3.SA',	'GMAT3.SA',	'RECV3.SA',	'DXCO3.SA',	'RAPT4.SA',	'TTEN3.SA',	'CXSE3.SA',	'PSSA3.SA',	'IRBR3.SA',	'ELET6.SA',	'CPFE3.SA',	'KLBN4.SA',	'BPAN4.SA',	'SMTO3.SA',	'EZTC3.SA',	'ABCB4.SA',	'ZAMP3.SA',	'SBFG3.SA',	'HBOR3.SA',	'EGIE3.SA',	'AMBP3.SA',	'DIRR3.SA',	'TRIS3.SA',	'CASH3.SA',	'GUAR3.SA',	'GGPS3.SA',	'MILS3.SA',	'ODPV3.SA',	'TUPY3.SA',	'SAPR4.SA',	'MEAL3.SA',	'CSMG3.SA',	'LIGT3.SA',	'MATD3.SA',	'CURY3.SA',	'DASA3.SA',	'NEOE3.SA',	'CAML3.SA',	'OPCT3.SA',	'ETER3.SA',	'RANI3.SA',	'PRNR3.SA',	'EVEN3.SA',	'AERI3.SA',	'CSED3.SA',	'INTB3.SA',	'GRND3.SA',	'LAVV3.SA',	'MDIA3.SA',	'PLPL3.SA',	'SOJA3.SA',	'BMGB4.SA',	'FESA4.SA',	'VLID3.SA',	'KRSA3.SA',	'JALL3.SA',	'MTRE3.SA',	'KEPL3.SA',	'AZEV3.SA',	'MYPK3.SA',	'SEER3.SA',	'LOGG3.SA',	'PNVL3.SA',	'VULC3.SA',	'SHOW3.SA',	'BRIT3.SA',	'AMAR3.SA',	'ITUB3.SA',	'TASA4.SA',	'VITT3.SA',	'MDNE3.SA',	'CMIG3.SA',	'TECN3.SA',	'PINE4.SA',	'ARML3.SA',	'MELK3.SA',	'NGRD3.SA',	'USIM3.SA',	'PGMN3.SA',	'TGMA3.SA',	'MBLY3.SA',	'PTBL3.SA',	'WIZC3.SA',	'JSLG3.SA',	'KLBN3.SA',	'ESPA3.SA',	'TFCO4.SA',	'ORVR3.SA',	'FRAS3.SA',	'LEVE3.SA',	'TAEE4.SA',	'SHUL4.SA',	'HBRE3.SA',	'FIQE3.SA',	'OIBR3.SA',	'PORT3.SA',	'BMOB3.SA',	'UNIP6.SA',	'SAPR3.SA',	'AGXY3.SA',	'AGRO3.SA',	'RNEW4.SA',	'RCSL4.SA',	'ITSA3.SA',	'POMO3.SA',	'ELMD3.SA',	'LPSB3.SA',	'SANB3.SA',	'SANB4.SA',	'DESK3.SA',	'BLAU3.SA',	'RCSL3.SA',	'PFRM3.SA',	'ROMI3.SA',	'TAEE3.SA',	'BRAP3.SA',	'GOAU3.SA',	'DEXP3.SA',	'VTRU3.SA',	'TCSA3.SA',	'BIOM3.SA',	'CSUD3.SA',	'PMAM3.SA',	'GGBR3.SA',	'INEP3.SA',	'ALPK3.SA',	'DEXP4.SA',	'LUPA3.SA',	'TPIS3.SA',	'TRAD3.SA',	'VIVR3.SA',	'CTSA4.SA',	'SYNE3.SA',	'CAMB3.SA',	'ALLD3.SA',	'ENGI4.SA',	'RNEW3.SA',	'EUCA4.SA',	'DMVF3.SA',	'IGTI3.SA',	'IGTI3.SA',	'TASA3.SA',	'LAND3.SA',	'AALR3.SA',	'UCAS3.SA',	'RSID3.SA',	'RPMG3.SA',	'SCAR3.SA',	'ALUP4.SA',	'NUTR3.SA',	'FHER3.SA',	'LVTC3.SA',	'BRKM3.SA',	'BMEB4.SA',	'ENGI3.SA',	'AVLL3.SA',	'WEST3.SA',	'BOBR4.SA',	'EPAR3.SA',	'BPAC3.SA',	'PDTC3.SA',	'BRSR3.SA',	'LOGN3.SA',	'CEBR6.SA',	'DOTZ3.SA',	'CSRN3.SA',	'EALT4.SA',	'ALUP3.SA',	'SGPS3.SA',	'BEES3.SA',	'RAPT3.SA',	'COCE5.SA',	'ALPA3.SA',	'ATOM3.SA',	'CGRA4.SA',	'UNIP3.SA',	'CGRA3.SA',	'BEES4.SA',	'NINJ3.SA',	'CEBR5.SA',	'NORD3.SA',	'INEP4.SA',	'CLSC4.SA',	'PTNT4.SA',	'BAZA3.SA',	'TELB4.SA',	'CEDO4.SA',	'BPAC5.SA',	'RDNI3.SA',	'TRPL3.SA',	'MGEL4.SA',	'HAGA4.SA',	'EMAE4.SA',	'DOHL4.SA',	'CGAS5.SA',	'EQPA3.SA',	'HAGA3.SA',	'VSTE3.SA',	'WHRL4.SA',	'CTNM4.SA',	'CEBR3.SA',	'MTSA4.SA',	'REDE3.SA',	'CTSA3.SA',	'WHRL3.SA',	'BMEB3.SA',	'CRPG5.SA',	'MNPR3.SA',	'EKTR4.SA',	'WLMM4.SA',	'UNIP5.SA',	'OIBR4.SA',	'RSUL4.SA',	'EQMA3B.SA',	'OFSA3.SA',	'EALT3.SA',	'EUCA3.SA',	'PTNT3.SA',	'CRPG6.SA',	'BSLI3.SA',	'SNSY3.SA',	'PINE3.SA',	'OSXB3.SA',	'RPAD6.SA',	'CGAS3.SA',	'GEPA4.SA',	'BALM4.SA',	'NEXP3.SA',	'PEAB3.SA',	'BGIP4.SA',	'BDLL4.SA',	'PLAS3.SA',	'ATMP3.SA',	'ENMT4.SA',	'BGIP3.SA',	'CEED3.SA',	'BSLI4.SA',	'ESTR4.SA',	'BNBR3.SA',	'APER3.SA',	'HBTS5.SA',	'COCE3.SA',	'BRSR5.SA',	'CTKA4.SA',	'TELB3.SA',	'CPLE5.SA',	'HETA4.SA',	'BMKS3.SA',	'SNSY5.SA',	'CSRN5.SA',	'FESA3.SA',	'BAHI3.SA',	'HOOT4.SA',	'CEDO3.SA',	'USIM6.SA',	'AHEB3.SA',	'CSRN6.SA',	'CEEB3.SA',	'IGTI4.SA',	'IGTI4.SA',	'CTNM3.SA',	'GEPA3.SA',	'CLSC3.SA',	'MAPT3.SA',	'BAUH4.SA',	'WLMM3.SA',	'MNDL3.SA',	'FRIO3.SA',	'AFLT3.SA',	'RPAD5.SA',	'ENMT3.SA',	'MAPT4.SA',	'MWET4.SA',	'LIPR3.SA',	'MRSA6B.SA',	'PATI3.SA',	'BALM3.SA',	'PSVM11.SA',	'EQPA5.SA',	'LUXM4.SA',	'BRKM6.SA',	'TEKA4.SA',	'MOAR3.SA',	'MERC4.SA',	'DTCY3.SA',	'MRSA3B.SA',	'FIEI3.SA',	'BMIN4.SA',	'ELET5.SA',	'BDLL3.SA',	'GSHP3.SA',	'MRSA5B.SA',	'RPAD3.SA',	'JOPA3.SA',	'BMIN3.SA',	'EKTR3.SA']
cripto = ['USDT-USD',	'BTC-USD',	'ETH-USD',	'USDC-USD',	'FDUSD-USD',	'SOL-USD',	'BNB-USD',	'XRP-USD',	'VBNB-USD',	'WETH-USD',	'SOL16116-USD',	'VBTC-USD',	'DOGE-USD',	'PEPE24478-USD',	'TON11419-USD',	'LTC-USD',	'VUSDT-USD',	'TRX-USD',	'WIF-USD',	'SUI20947-USD',	'WBTC-USD',	'AAVE-USD',	'MATIC-USD',	'RUNE-USD',	'ADA-USD',	'AVAX-USD',	'BOME-USD',	'BCH-USD',	'LINK-USD',	'NOT-USD',	'CRV-USD',	'FTN-USD',	'NEAR-USD',	'FTM-USD',	'SHIB-USD',	'ARB11841-USD',	'1000SATS-USD',	'SATS28194-USD',	'OP-USD',	'VETH-USD',	'APT21794-USD',	'FLOKI-USD',	'VUSDC-USD',	'WBNB-USD',	'BONK-USD',	'MNT27075-USD',	'DAI-USD',	'ATOM-USD',	'ORDI-USD',	'DOT-USD',	'TIA22861-USD',	'USDCE-USD',	'ONDO-USD',	'MEW30126-USD',	'ETC-USD',	'BANANA28066-USD',	'FET-USD',	'WEETH-USD',	'T-USD',	'ATH30083-USD',	'UNI7083-USD',	'EOS-USD',	'FIL-USD',	'ZEC-USD',	'INJ-USD',	'GALA-USD',	'QKC-USD',	'WLD-USD',	'ZRO26997-USD',	'MAX32506-USD',	'STX4847-USD',	'JUP29210-USD',	'USDE29470-USD',	'IO29835-USD',	'SAGA30372-USD',	'LDO-USD',	'KAS-USD',	'WSTETH-USD',	'ETHFI-USD',	'JASMY-USD',	'VCAKE28404-USD',	'TURBO-USD',	'MBL-USD',	'PEOPLE-USD',	'SEI-USD',	'ENS-USD',	'STETH-USD',	'RARE11294-USD',	'CORE23254-USD',	'MKR-USD',	'STRK22691-USD',	'ZETA-USD',	'TAO22974-USD',	'POPCAT28782-USD',	'XMR-USD',	'NAKA-USD',	'ICP-USD',	'PENDLE-USD']
fii = ['XPML11.SA', 'KNCR11.SA', 'MXRF11.SA', 'BTLG11.SA', 'TRXF11.SA', 'TGAR11.SA', 'KNIP11.SA', 'HGLG11.SA', 'CPTS11.SA', 'VISC11.SA', 'PVBI11.SA', 'HBCR11.SA', 'XPLG11.SA', 'KNRI11.SA', 'GARE11.SA', 'CPOF11.SA', 'LVBI11.SA', 'JCCJ11.SA', 'MCHY11.SA', 'RZTR11.SA', 'KNHY11.SA', 'RBRY11.SA', 'HGBS11.SA', 'HSML11.SA', 'VGHF11.SA', 'IRDM11.SA', 'VGIR11.SA', 'MALL11.SA', 'BRCO11.SA', 'MCCI11.SA', 'KNHF11.SA', 'HGRU11.SA', 'KNSC11.SA', 'RBRR11.SA', 'KNCA11.SA', 'RURA11.SA', 'CVBI11.SA', 'CPSH11.SA', 'RECR11.SA', 'HGCR11.SA', 'BCFF11.SA', 'RBRF11.SA', 'RZAK11.SA', 'JCIN11.SA', 'JSAF11.SA', 'KNUQ11.SA', 'TRXB11.SA', 'VILG11.SA', 'JSRE11.SA', 'SNAG11.SA', 'KORE11.SA', 'XPCI11.SA', 'HFOF11.SA', 'ITRI11.SA', 'ALZR11.SA', 'VGIA11.SA', 'BTCI11.SA', 'RZAG11.SA', 'VCJR11.SA', 'CLIN11.SA', 'VRTA11.SA', 'BRCR11.SA', 'URPR11.SA', 'GGRC11.SA', 'TEPP11.SA', 'HGRE11.SA', 'LASC11.SA', 'CACR11.SA', 'VGIP11.SA', 'RVBI11.SA', 'BPML11.SA', 'KFOF11.SA', 'XPCA11.SA', 'HABT11.SA', 'RBVA11.SA', 'AFHI11.SA', 'RBRP11.SA', 'FGAA11.SA', 'HCTR11.SA', 'RBRX11.SA', 'VINO11.SA', 'EVBI11.SA', 'GZIT11.SA', 'HSRE11.SA', 'FATN11.SA', 'TVRI11.SA', 'HGPO11.SA', 'DEVA11.SA', 'SARE11.SA', 'GTWR11.SA', 'AAZQ11.SA', 'SPXS11.SA', 'VVMR11.SA', 'OUJP11.SA',  'TRBL11.SA', 'CPTR11.SA', 'VCRA11.SA', 'GSFI11.SA', 'BARI11.SA', 'BCIA11.SA', 'HSAF11.SA', 'HTMX11.SA', 'RCRB11.SA', 'CRAA11.SA', 'KISU11.SA', 'HSLG11.SA', 'AJFI11.SA', 'RZEO11.SA', 'BLMG11.SA', 'BTAL11.SA', 'VGRI11.SA', 'MFII11.SA', 'NEWL11.SA', 'ICRI11.SA', 'XPIN11.SA', 'BBIG11.SA', 'MANA11.SA', 'HGFF11.SA', 'HPDP11.SA', 'BROF11.SA', 'BTYU11.SA', 'EGAF11.SA', 'CCME11.SA', 'XPSF11.SA', 'KIVO11.SA', 'JGPX11.SA']
etf_us = ['SQQQ',	'SOXL',	'SOXS',	'TQQQ',	'TSLL',	'NVD',	'SPY',	'IWM',	'HYG',	'QQQ',	'SH',	'SPXS',	'TLT',	'FXI',	'TZA',	'NVDL',	'XLF',	'LQD',	'EEM',	'TNA',	'SLV',	'IBIT',	'BKLN',	'DUST',	'GDX',	'KRE',	'UVIX',	'KWEB',	'EWZ',	'LABD',	'SDOW',	'NVDQ',	'TECS',	'TMF',	'ETH',	'UVXY',	'VCSH',	'BOIL',	'XRT',	'EFA',	'NVDX',	'USHY',	'YANG',	'SPXU',	'XLU',	'VWO',	'VCIT',	'SDS',	'GLDM',	'USFR',	'XLE',	'VXX',	'BITX',	'SVIX',	'MSOS',	'SMH',	'QID',	'PSQ',	'IEFA',	'XLP',	'ARKK',	'RSP',	'UNG',	'XLRE',	'XBI',	'IJH',	'GOVT',	'QYLD',	'BIL',	'TSLT',	'VCLT',	'IEMG',	'XLI',	'XLV',	'FAZ',	'GLD',	'AGG',	'YINN',	'BITO',	'BND',	'EWJ',	'UPRO',	'IEF',	'VIXY',	'TSLZ',	'VEA',	'SGOL',	'JPST',	'SVXY',	'TWM',	'BITI',	'IAU',	'IYR',	'VOO',	'SPLG',	'SJNK',	'SGOV',	'IJR',	'VTEB',	'BTC']
etf_br = ['BOVA11.SA', 'ALUG11.SA', 'B5P211.SA', 'BBOV11.SA', 'BITH11.SA', 'BOVB11.SA', 'BOVV11.SA', 'BOVX11.SA', 'BTEK11.SA', 'CORN11.SA', 'DIVO11.SA', 'ESGU11.SA', 'ETHE11.SA', 'EURP11.SA', 'FIND11.SA', 'GOLD11.SA', 'HASH11.SA', 'IBOB11.SA', 'IMAB11.SA', 'IVVB11.SA', 'LFTS11.SA', 'MATB11.SA', 'NASD11.SA', 'PIBB11.SA', 'QBTC11.SA', 'QETH11.SA', 'SMAC11.SA', 'SMAL11.SA', 'SPXI11.SA', 'TRIG11.SA', 'USAL11.SA', 'UTEC11.SA', 'WRLD11.SA', 'XFIX11.SA', 'XINA11.SA']
commodites = ['ES=F',	'YM=F',	'NQ=F',	'RTY=F',	'ZB=F',	'ZN=F',	'ZF=F',	'ZT=F',	'GC=F',	'MGC=F',	'SI=F',	'SIL=F',	'PL=F',	'HG=F',	'PA=F',	'CL=F',	'HO=F',	'NG=F',	'RB=F',	'BZ=F',	'B0=F',	'ZC=F',	'ZO=F',	'KE=F',	'ZR=F',	'ZM=F',	'ZL=F',	'ZS=F',	'GF=F',	'HE=F',	'LE=F',	'CC=F',	'KC=F',	'CT=F',	'LBS=F',	'OJ=F',	'SB=F']
stocks = ['NVDA',	'TSLA',	'ASTS',	'RKLB',	'PLTR',	'PFE',	'RIVN',	'INTC',	'AAPL',	'NU',	'BBD',	'MARA',	'AMD',	'AAL',	'ABEV',	'GRAB',	'LUMN',	'BABA',	'NIO',	'AMZN',	'LCID',	'JD',	'GOOGL',	'F',	'CSCO',	'WBD',	'SOFI',	'SNAP',	'GOLD',	'CLSK',	'MU',	'BAC',	'CCL',	'CMG',	'AVGO',	'T',	'ET',	'ITUB',	'PBR',	'LYFT',	'VALE',	'MSFT',	'AMCR',	'GOOG',	'META',	'MRVI',	'RIOT',	'WMT',	'BMY',	'SBUX',	'AMAT',	'NKE',	'SIRI',	'GTES',	'NGD',	'DELL',	'GM',	'HOOD',	'CX',	'ERIC',	'MSTR',	'CORZ',	'MRVL',	'BTG',	'BCS',	'WFC',	'VTRS',	'UMC',	'KGC',	'SMCI',	'IAG',	'UAA',	'VZ',	'RIG',	'SWN',	'TSM',	'PDD',	'LI',	'NCLH',	'TME']
fii_with_suffix = [code.replace('11', '11.SA') for code in fii]

if ticker == tickers[0]:
    ticker_id = acoes
elif ticker == tickers[1]:
    ticker_id = cripto
elif ticker == tickers[2]:
    ticker_id = fii
elif ticker == tickers[3]:
    ticker_id = etf_us
elif ticker == tickers[4]:
    ticker_id = etf_br
elif ticker == tickers[5]:
    ticker_id = commodites
elif ticker == tickers[6]:
    ticker_id = stocks
else:
    print("Erro: Opção inválida.")
    time.sleep(3)
    exit()

#Input's
end = input("Digite a data de consulta (yyyy-mm-dd): ")
window = int(input('Periodo Média Móvel: '))
historico = int(input("Histórico do indicador (Exemplo: D-5 (Digite apenas o número)): "))


# Define a data de consulta

end = datetime.strptime(end, '%Y-%m-%d')
start = (end - timedelta(days = 252)).strftime('%Y-%m-%d')

# Carrega os preços dos ativos
volume = yf.download(ticker_id, start = start, end = end)['Volume']
precos = yf.download(ticker_id, start = start, end = end)['Adj Close']

#Média Móvel
media_volume = volume.rolling(window = window).mean()
media_volume = media_volume.tail(historico)

#Desvio Padrao
desvio_volume = volume.rolling(window = window).std()
desvio_volume = desvio_volume.tail(historico)

# Iterar pelas colunas dos DataFrames - Banda de STD
banda1std = pd.DataFrame()
banda2std = pd.DataFrame()
banda3std = pd.DataFrame()

for coluna in media_volume.columns:
    # Multiplicar a coluna atual de df1 e df2
    banda1std[f'{coluna}'] = media_volume[coluna] + 1.5 * desvio_volume[coluna]

for coluna in media_volume.columns:
    # Multiplicar a coluna atual de df1 e df2
    banda2std[f'{coluna}'] = media_volume[coluna] + 2.5 * desvio_volume[coluna]

for coluna in media_volume.columns:
    # Multiplicar a coluna atual de df1 e df2
    banda3std[f'{coluna}'] = media_volume[coluna] + 3.5 * desvio_volume[coluna]

# Ajusta dataframe volume
volume  = volume.iloc[::-1]
volume_head = volume.head(historico)

#Screening Banda1std
banda1std = banda1std.iloc[::-1]
resultado1 = (volume_head > banda1std).T

#Screening Banda2std
banda2std = banda2std.iloc[::-1]
resultado2 = (volume_head > banda2std).T

#Screening Banda2std
banda3std = banda3std.iloc[::-1]
resultado3 = (volume_head > banda3std).T

#Verificação de sinais no histórico selecionado
resultado1.insert(0, 'Count_True', resultado1.apply(lambda row: row.sum(), axis=1))
resultado2.insert(0, 'Count_True', resultado2.apply(lambda row: row.sum(), axis=1))
resultado3.insert(0, 'Count_True', resultado3.apply(lambda row: row.sum(), axis=1))

#Vericação de sinais no dia mais recente
resultado1.insert(0, 'Recent_Signal', resultado1.iloc[:, 1].apply(lambda x: 1 if x else 0))
resultado2.insert(0, 'Recent_Signal', resultado2.iloc[:, 1].apply(lambda x: 1 if x else 0))
resultado3.insert(0, 'Recent_Signal', resultado3.iloc[:, 1].apply(lambda x: 1 if x else 0))

#Importando para excel
with pd.ExcelWriter('screening.xlsx', engine = 'xlsxwriter') as writer:
    # Escreve cada banda em uma aba separada
    resultado1.to_excel(writer, sheet_name = 'Banda1STD', index = True)
    resultado2.to_excel(writer, sheet_name = 'Banda2STD', index = True)
    resultado3.to_excel(writer, sheet_name = 'Banda3STD', index = True)
