###----------[ AUTHOR & CREATOR ]---------- ###
# ------ [ Gausah Dioprek Ntar Error ] ------ #
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'

###----------[ IMPORT MODULE ]---------- ###
import requests,bs4,sys,os,re
from bs4 import BeautifulSoup as bs

###----------[ BERSIHKAN TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

###----------[ LOOPING ]---------- ###
loop = 0
fail = 0

###----------[ KOMENTAR OTOMATIS ]---------- ###
def random_komen_bucin(target):
    komen = [
        'Aku mau bilang sama kamu, sebenernya aku itu sayang banget sama kamu %s. Udh lama aku nyimpen perasaan ini, tapi gaberani ngungkapin. Semoga kamu bisa nebak siapa aku. I Love You %s.'%(target,target),
        'I Have Crush On You. Aku gaberani ngungkapin secara langsung karena takut kamu tolak. Tapi yang jelas, aku mengagumimu wahai %s. Semoga kamu bahagia selalu.'%(target),
        'Aku gatau gimana bilangnya, tapi dari lama aku suka sama kamu, %s. Andai kamu tau, aku simpen semua foto-foto yang kamu post di sosmedmu. Aku harap bisa kenal lebih deket sama kamu.'%(target),
        'Jangan lupa bahagia ya %s. Jangan pernah sedih ketika menghadapi hari yang buruk, Masih ada aku disini yang bakalan support kamu terus. Love You %s.'%(target,target),
        'Kalau harimu buruk, aku mau kok nemenin kamu %s. Jadikan aku tempat curhatmu, tempat berkeluh kesahmu. I Always Support You. Salam hangat buat kamu %s.'%(target,target),
        'Baru kali ini aku nemu orng sebaik kamu, udh baik cakep lagi, kan rasa ingin memiliki ini jadi tinggi. Boleh ga si aku jujur kalau aku suka sama kamu %s.'%(target),
        'Banyak banget ya ternyata yang suka sama kamu di secreto ini. Tapi gapapa, aku bakalan buktiin bahwa akulah yg paling pantes dapetin kamu, wahai %s idamanku. Kamulah yg terbaik.'%(target),
        'Boleh ga si aku cemburu kalau kamu deket sama cwo lain, karna akunya ada rasa sama kamu %s. Pasti jawabannya gaboleh, tpi aku tetap nekat mencintaimu dalam diam.'%(target),
        'Kamu jangan sedih soal masa lalumu. Inget masa depanmu msh panjang. Kalau dia nyakitin, berarti dia bukan jodohmu. Karena jodohmu itu cuma aku wkwkwk. Love %s.'%(target),
        'Tetap semangat menjalani hari2nya yaa, aku cuma bisa berdoa supaya aku & %s bisa lebih deket. Kita udah kenal deket, tapi akunya gaberani bilang kalau ada rasa sama %s.'%(target,target)]
    return(komen)
def random_komen_toxic(target):
    komen = [
        'Yaelah dek, lu tuh gak lebih dari seorang wibu nolep tukang ngocok. Inget ya dek %s, lo tuh cuman sampah gaguna! Pergi aja lo dari dunia ini cuihhh!'%(target),
        'Woy cil, sadar diri mukalu kek babi! Gak good looking sok-sokan najis ewh. Dek %s, mending lo mati aja deh klo kata gw.'%(target),
        'Wkwkwk lonte lacur sasimo, deketin banyak orang buat pelampiasan. Sadar diri mukalu kek daki, gila lu dek %s pengen dapetin banyak pasangan. Najis yahaha.'%(target),
        'Gw benci samalu, semoga keluargalu mati kecelakaan, sampe sisa lu seorang diri hidup sebatang kara jadi gelandangan. Najis samalu %s anjing bangsat!'%(target),
        'Oalah jadi ini orangnya, banyak gaya amat sih dek. Lu tuh gada apa-apanya dibanding gw. Inget ya bocah %s, lu itu ga lebih dari seorang sampah gaguna!'%(target),
        'Mental sosmed doang lu bocah %s, yok sini meet klo berani. Udh muka kek daki di kontol, sifat kek lonte biadab, mati ajalu sampah!'%(target),
        'Gw lihat isi secreto lu isinya hate komen semua wkwkwk. Rasain lo %s, mati ajalo, kelakuanlo emang kek kontol kaga bisa dimaafin %s anjing babi memek!'%(target,target),
        'Gw pengen lu ilang dari dunia ini, lu ga lebih dari seorang sampah pengacau. Inget %s, lo itu adalah seburuk2nya dan serendah2nya manusia. %s idiot anjing babi bangsat kontol!'%(target,target),
        'Woy %s lonte sasimo, gw heran kok ada juga orng yg modelannya kek elu, dan lbh herannya lagi bnyk yg suka wkwkwk. Goblok tolol najisun lo %s anjing cuihh.'%(target,target),
        'Janji ga kena mental? Bruakakak %s mending apus secretolu, gaada yg seneng samalo di dunia ini. Mati aja lo %s anjing bangsaatttt!'%(target,target)]
    return(komen)
def random_komen_support(target):
    komen = [
        '%s kamu yg semangat yaa jalanin hari2nya. Bahagia selalu buatmu!'%(target),
        'Jangan sedih2 dong %s, nanti cakepnya ilang loh. Kami disini selalu support kamu!'%(target),
        'Kamu ngerti ga si %s, kamutu gapantes sedih2. Tinggalin yg buat kamu sedih, deketin aku yg bikin kamu bahagia wkwk.'%(target),
        'Allah adalah sebaik2nya tempat pelarian ketika kamu sedih. Jangan selfharm ya %s cakeeep!'%(target),
        'Woy %s, masa depanmu msh panjang. Kamu skrng gausa mikirin hal yg engga2 dlu. Fokus sama masa depanmu, semangat!'%(target),
        'Semangat %s, gausa dengerin perkataan orang yg nyakitin kamu. Anggep aja angin lewat.'%(target),
        'Ayolah, kau pasti bisa lewatin semua ini. Ingat, msh ada cita-cita yang harus kamu wujudkan! Semangat %s!'%(target),
        'Allah tidak akan memberikan cobaan diluar batas kemampuan makhluknya, stay strong %s!'%(target),
        'Mungkin kamu gakenal aku, tapi aku kenal kamu. Aku bakalan terus support kamu secara diam-diam. Love u %s! Tetap semangat yaa!'%(target),
        'Kegagalan hari ini adalah awal dari keberhasilan hari esok, gaada kata terlambat untuk berbuat. Pegang teguh pendirianmu %s.'%(target)]
    return(komen)
def random_komen_random(target):
    komen = [
        'P info ngab %s'%(target),
        'Adkh ingfo cuy',
        'No ingfo okoklh',
        'Ancrit bet beliau ini',
        'Hi lord %s'%(target),
        'Lari ada wibu',
        'Gabut kh cuy?',
        'Lagi apa cuy?',
        'Mantap min',
        'Ingfo bandar %s'%(target)]
    return(komen)

###----------[ MENU ]---------- ###
class menu_secreto:
    def __init__(self):
        global url
        print('[ Bot Secreto ]\n')
        url = input('Masukkan URL : ')
        self.scrap_url(url)
    def scrap_url(self,url):
        hea = {
            'Referer'                   : url,
            'sec-ch-ua'                 : '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile'          : '?1',
            'sec-ch-ua-platform'        : "Android",
            'Upgrade-Insecure-Requests' : '1',
            'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'}
        with requests.Session() as xyz:
            try:
                req = bs(xyz.get(url, headers=hea).content,'html.parser')
                nam = req.find('h2',id='user_name')
                print('Secreto Milik %s'%(nam.text))
                self.menu()
            except: exit('\nTerjadi Kesalahan')
    def menu(self):
        print('\n[ Menu ]')
        print('[1] Bot Komentar')
        print('[2] Cek Pesan')
        #print('[3] Balas Pesan')
        d = input('Pilih : ')
        print('')
        if d in ['1','01','a']:self.menu_bot_komen()
        elif d in ['2','02','b']:cek_pesan()
        elif d in ['3','03','c']:balas_komen()
        else:exit('Isi Yg Benar!')
    def menu_bot_komen(self):
        print('[ Menu Bot Komen ]')
        print('[1] Komentar Manual')
        print('[2] Komentar Otomatis')
        e = input('Pilih : ')
        print('')
        if e in ['1','01','a']:self.bot_komen_manual()
        elif e in ['2','02','b']:self.bot_komen_otomatis()
        else:exit('Isi Yg Benar!')
    def bot_komen_manual(self):
        print('Beda Komentar Pisahkan Dengan Koma (,)')
        kom = input('Tulis Komentar : ').split(',')
        jum = input('Berapa Kelipatan Komentar : ')
        print('Total Komentar : %s'%(str(int(jum)*len(kom))))
        for x in range(int(jum)):
            for y in kom:
                send_secreto(y)
    def bot_komen_otomatis(self):
        print('[ Menu Komentar ]')
        print('[1] Komentar Bucin')
        print('[2] Komentar Toxic')
        print('[3] Komentar Support')
        print('[4] Komentar Random')
        f = input('Pilih : ')
        print('')
        tar = input('Nama Target : ')
        jum = input('Berapa Kelipatan Komentar : ')
        print('Total Komentar : %s'%(str(int(jum)*10)))
        if f in ['1','01','a']:
            for x in range(int(jum)):
                for y in random_komen_bucin(tar):
                    send_secreto(y)
        elif f in ['2','02','b']:
            for x in range(int(jum)):
                for y in random_komen_toxic(tar):
                    send_secreto(y)
        elif f in ['3','03','c']:
            for x in range(int(jum)):
                for y in random_komen_support(tar):
                    send_secreto(y)
        elif f in ['4','04','d']:
            for x in range(int(jum)):
                for y in random_komen_random(tar):
                    send_secreto(y)
        else:exit('Isi Yg Benar!')
        
###----------[ KIRIM PESAN ]---------- ###
class send_secreto:
    def __init__(self,pesan):
        self.main(pesan)
    def main(self,pesan):
        global loop,fail
        hea = {
            'Referer'                   : url,
            'sec-ch-ua'                 : '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile'          : '?1',
            'sec-ch-ua-platform'        : "Android",
            'Upgrade-Insecure-Requests' : '1',
            'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'}
        with requests.Session() as xyz:
            req = xyz.get(url, headers=hea)
            raq = bs(req.content,'html.parser')
            cok = xyz.cookies.get_dict()
            tam = raq.find('div',id='form')
            data = {
                'XSRF-TOKEN'      : cok['XSRF-TOKEN'],
                'laravel_session' : cok['laravel_session'],
                'id'              : re.search('<span class="hidden" id="id">(.*?)</span>',str(tam)).group(1),
                'message'         : pesan,
                'send_message'    : True}
            jan = xyz.post('https://api.secreto.site/sendmsg',data=data,headers=hea)
            if str(jan) == '<Response [200]>': loop += 1
            else: fail += 1
            print('\rBerhasil [%s] Gagal [%s]'%(str(loop),str(fail)),end='');sys.stdout.flush()

###----------[ CEK PESAN ]---------- ###
class cek_pesan:
    def __init__(self):
        self.main()
    def main(self):
        gka = 0
        hea = {
            'Referer'                   : url,
            'sec-ch-ua'                 : '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile'          : '?1',
            'sec-ch-ua-platform'        : "Android",
            'Upgrade-Insecure-Requests' : '1',
            'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'}
        with requests.Session() as xyz:
            req = bs(xyz.get(url, headers=hea).content,'html.parser')
            for x in req.find_all('div',class_='main-message-box'):
                try:
                    gka += 1
                    tyu = x.find('h6').text
                    print('[%s] %s'%(str(gka),tyu))
                except: pass

###----------[ BALAS KOMEN ]---------- ###
class balas_komen:
    def __init__(self):
        self.main()
    def main(self):
        global loop,fail
        hea = {
            'Referer'                   : url,
            'sec-ch-ua'                 : '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile'          : '?1',
            'sec-ch-ua-platform'        : "Android",
            'Upgrade-Insecure-Requests' : '1',
            'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'}
        with requests.Session() as xyz:
            req = xyz.get(url, headers=hea)
            raq = bs(req.content,'html.parser')
            cok = xyz.cookies.get_dict()
            for x in raq.find_all('div',class_='main-message-box'):
                try:
                    tyu = x.find('form')
                    ids = re.search('"true" id="(.*?)"',str(tyu)).group(1)
                    data = {
                        'XSRF-TOKEN'      : cok['XSRF-TOKEN'],
                        'laravel_session' : cok['laravel_session'],
                        'id'              : 'ar0235',
                        ids               : 'Ah Yg Bener',
                        'comments_'+ids   : True}
                    jan = xyz.post('https://api.secreto.site/sendcomment',data=data,headers=hea)
                    if str(jan) == '<Response [200]>': loop += 1
                    else: fail += 1
                    print('\rBerhasil [%s] Gagal [%s]'%(str(loop),str(fail)),end='');sys.stdout.flush()
                except Exception as e: print(e)

###----------[ TRIGGER ]---------- ###
if __name__ == '__main__':
    resik()
    menu_secreto()
    exit('\n')