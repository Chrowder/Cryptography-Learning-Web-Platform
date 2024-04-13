from pycipher import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score
fitness = ngram_score('quadgrams.txt') # load our quadgram statistics

# ctext='pmpafxaikkitprdsikcplifhwceigixkirradfeirdgkipgigudkcekiigpwrpucikceiginasikwduearrxiiqepcceindgmieinpwdfprduppcedoikiqiasafmfddfipfgmdafmfdteiki'

ctext = """
SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAK OXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ
"""

ctext = """
Pfc x chyxl fp gfk vunvmzmumzfs yzlghcv kfcw, vhh ghch.

Mgh Vztlbh vunvmzmumzfs yzlghc zv fsh fp mgh vztlbhvm yzlghcv, vztlbh hsfuog mgxm zm yxs uvuxbbd nh ncfwhs kzmg lhs xsa lxlhc zs x phk tzsumhv. Fs mgzv lxoh kh kzbb pfyuv fs xumftxmzy ycdlmxsxbdvzv fp vunvmzmumzfs yzlghcv, z.h. kczmzso lcfocxtv mf vfbeh mghvh yzlghcv pfc uv.

Mgh vunvmzmumzfs yzlghc zv tfch yftlbzyxmha mgxs mgh Yxhvxc xsa Xppzsh yzlghcv. Zs mgfvh yxvhv, mgh sutnhc fp whdv khch 25 xsa 311 chvlhymzehbd. Mgzv xbbfkha x ncumh pfcyh vfbumzfs fp mcdzso xbb lfvvznbh whdv. Mgh sutnhc fp whdv lfvvznbh kzmg mgh vunvmzmumzfs yzlghc zv tuyg gzoghc, xcfusa 2^88 lfvvznbh whdv. Mgzv thxsv kh yxssfm mhvm mght xbb, kh gxeh mf 'vhxcyg' pfc offa whdv.

Kh kzbb nh uvzso x 'gzbb-ybztnzso' xbofczmgt mf pzsa mgh yfcchym whd. Pfc mgzv xllcfxyg, kh shha x kxd fp ahmhctzszso gfk vztzbxc x lzhyh fp mhjm zv mf hsobzvg mhjm. Mgzv zv yxbbha cxmzso mgh 'pzmshvv' fp mgh mhjm. X lzhyh fp mhjm ehcd vztzbxc mf hsobzvg kzbb ohm x gzog vyfch (x gzog pzmshvv), kgzbh x qutnbh fp cxsaft ygxcxymhcv kzbb ohm x bfk vyfch (x bfk pzmshvv). Pfc mgzv kh kzbb uvh x pzmshvv thxvuch nxvha fs ruxaocxt vmxmzvmzyv. Pfc x ouzah fs gfk mf ohshcxmh ruxaocxt vmxmzvmzyv, xsa vfth ldmgfs yfah pfc cxmzso mgh pzmshvv fp mhjm, vhh mgzv mumfczxb. Mgzv thmgfa kfcwv nd pzcvm ahmhctzszso mgh vmxmzvmzyv fp hsobzvg mhjm, mghs yxbyubxmzso mgh lcfnxnzbzmd mgxm mgh yzlghcmhjm yfthv pcft mgh vxth azvmcznumzfs. Xs zsyfcchymbd ahyzlghcha (z.h. uvzso mgh kcfso whd) thvvxoh kzbb lcfnxnbd yfsmxzs vhruhsyhv h.o. 'RWLY' kgzyg xch ehcd cxch zs sfctxb hsobzvg. Zs mgzv kxd kh yxs cxsw azpphchsm ahycdlmzfs whdv, mgh ahycdlmzfs whd kh kxsm zv mgh fsh mgxm lcfauyhv ahyzlghcha mhjm kzmg mgh gzoghvm bzwhbdgffa.

Mgh gzbb-ybztnzso xbofczmgt bffwv bzwh mgzv:

Ohshcxmh x cxsaft whd, yxbbha mgh 'lxchsm', ahyzlghc mgh yzlghcmhjm uvzso mgzv whd. Cxmh mgh pzmshvv fp mgh ahyzlghcha mhjm, vmfch mgh chvubm.
Ygxsoh mgh whd vbzogmbd (vkxl mkf ygxcxymhcv zs mgh whd xm cxsaft), thxvuch mgh pzmshvv fp mgh ahyzlghcha mhjm uvzso mgh shk whd.
Zp mgh pzmshvv zv gzoghc kzmg mgh tfazpzha whd, azvyxca fuc fba lxchsm xsa vmfch mgh tfazpzha whd xv mgh shk lxchsm.
Of nxyw mf 2, usbhvv sf ztlcfehthsm zs pzmshvv fyyuccha zs mgh bxvm 1000 zmhcxmzfsv.
Xv mgzv ydybh lcfyhhav, mgh ahyzlghcha mhjm ohmv pzmmhc xsa pzmmhc, mgh whd nhyfthv nhmmhc usmzb hzmghc mgh vfbumzfs xllhxcv, fc, mgh vfbumzfs zv sfm pfusa. Zs mgzv yxvh mgh cus gxv pxzbha xsa tuvm nh chlhxmha kzmg x azpphchsm vmxcmzso whd. Mgzv thxsv mgh gzbb-ybztnzso xbofczmgt zv vmuyw zs x 'bfyxb txjztut', kghch mghch xch sf vztlbh ygxsohv mgxm yxs nh txah mf mgh whd mf ztlcfeh pzmshvv, xsa dhm zm zv sfm xm mgh mcuh vfbumzfs. Zp mgzv gxllhsv dfu yxs cus mgh xbofczmgt xoxzs kzmg x azpphchsm lxchsm zs mgh gflh zm txd chxyg mgh mcuh vfbumzfs mgzv mzth. Zs mgh ztlbhthsmxmzfs nhbfk, kh txd chvmxcm mgh xbofczmgt 100'v fp mzthv zs mgh vhxcyg pfc mgh nhvm whd.

"""

ctext = re.sub('[^A-Z]','',ctext.upper())

maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
maxscore = -99e9
parentscore,parentkey = maxscore,maxkey[:]
print ("Substitution Cipher solver, you may have to wait several iterations")
print ("for the correct result. Press ctrl+c to exit program.")
# keep going until we are killed by the user
i = 0
while 1:
    i = i+1
    random.shuffle(parentkey)
    deciphered = SimpleSub(parentkey).decipher(ctext)
    parentscore = fitness.score(deciphered)
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        child = parentkey[:]
        # swap two characters in the child
        child[a],child[b] = child[b],child[a]
        deciphered = SimpleSub(child).decipher(ctext)
        score = fitness.score(deciphered)
        # if the child was better, replace the parent with it
        if score > parentscore:
            parentscore = score
            parentkey = child[:]
            count = 0
        count = count+1
    # keep track of best score seen so far
    if parentscore>maxscore:
        maxscore,maxkey = parentscore,parentkey[:]
        print ('\nbest score so far:',maxscore,'on iteration',i)
        ss = SimpleSub(maxkey)
        print ('    best key: '+''.join(maxkey))
        print ('    plaintext: '+ss.decipher(ctext))


