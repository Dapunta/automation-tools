import os, sys, requests, re, uuid
from bs4 import BeautifulSoup as bs

UserAgentWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
HeadersGet = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':UserAgentWindows}
HeadersPost = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Origin':'https://ngl.link','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':UserAgentWindows,'X-Requested-With':'XMLHttpRequest' }

def clear(): os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def KomentarBucin(target):
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
def KomentarToxic(target):
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
def KomentarSupport(target):
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
def KomentarRandom(target):
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

class NGL_Link():

    def __init__(self):
        self.InsertLink()
        self.InsertComment()
        self.LoopComment()
        self.SortExecution()
    
    def InsertLink(self):
        print('Masukkan Link NGL')
        print('Banyak Link, Pisahkan Dengan Koma (,)')
        self.ListLink = input('Masukkan Link : ').split(',')
        print('')
    
    def InsertComment(self):
        print('[ Menu Komentar ]')
        print('[1] Bucin  [3] Support  [5] Manual')
        print('[2] Toxic  [4] Random')
        try: km = int(input('Pilih : '))
        except Exception as e: exit('\nIsi Yg Benar!')
        if (1 <= km <= 4): target = input('\nMasukkan Nama Target : ')
        print('')
        if   km == 1: self.ListKomentar = KomentarBucin(target)
        elif km == 2: self.ListKomentar = KomentarToxic(target)
        elif km == 3: self.ListKomentar = KomentarSupport(target)
        elif km == 4: self.ListKomentar = KomentarRandom(target)
        elif km == 5:
            print('Banyak Komentar, Pisahkan Dengan (&&&)')
            self.ListKomentar = input('Tulis Komentar : ').split('&&&')
            print('')
        else: exit('Isi Yg Benar!')

    def LoopComment(self):
        self.LoopKomentar = int(input('Ulangi Komentar Berapa Kali : '))
        print('')

    def SortExecution(self):
        self.TotalLoop = len(self.ListLink) * len(self.ListKomentar) * self.LoopKomentar
        self.LoopSekarang = 0
        self.SuccessLoop = 0
        self.FailedLoop = 0
        for link in self.ListLink:
            for loop in range(self.LoopKomentar):
                for comment in self.ListKomentar:
                    self.Execution(link,comment)

    def Execution(self,link,comment):
        try:
            r = requests.Session()
            req = r.get(link,headers=HeadersGet).text
            username = re.search('var username = "(.*?)"',str(req)).group(1)
            dta = {'username':username,'question':comment,'deviceId':str(uuid.uuid4()),'gameSlug':'','referrer':''   }
            pos = r.post('https://ngl.link/api/submit',data=dta,headers=HeadersPost).text
            if 'questionId' in str(pos): self.SuccessLoop += 1
            else: self.FailedLoop += 1
        except Exception as e: self.FailedLoop += 1
        self.LoopSekarang += 1
        print('\rProses [%s/%s] Berhasil:%s Gagal:%s'%(str(self.LoopSekarang),str(self.TotalLoop),str(self.SuccessLoop),str(self.FailedLoop)),end=''); sys.stdout.flush()
            

if __name__ == '__main__':
    clear()
    NGL_Link()

# https://ngl.link/ratyanonim