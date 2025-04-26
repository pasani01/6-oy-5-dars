from django.shortcuts import render

peoples=[
    {
        'name':'Ali Şir Nevai',
        'about':"Türk edebiyatının büyük şairlerinden biridir. Çağatay Türkçesi'ni edebi bir dil haline getirmiştir. Şiirlerinde aşk, insanlık ve bilgelik temalarını işlemiştir. 'Muhakemetü’l-Lügateyn' adlı eseriyle Türkçenin üstünlüğünü savunmuştur.",
        'img':'NEVAI.JPEG'
    },
    {
        'name':'Ahmet Yesevi',
        'about':'Türk dünyasının ilk büyük mutasavvıf şairidir. Tasavvufu Orta Asya’da yaygınlaştırmıştır. "Divan-ı Hikmet" adlı eseriyle insanlara dini ve ahlaki öğütler vermiştir. Türklerin İslamlaşmasında önemli rol oynamıştır.',
        'img':'YESEVI.JPEG'
    },
    {
        'name':'Mahmud Kaşgarî',
        'about':'Ünlü dil bilimci ve sözlük yazarıdır. Türk lehçelerini derleyip "Divânu Lügatit-Türk" adlı ilk Türkçe sözlüğü yazmıştır. Türk kültürü, dili ve coğrafyası hakkında değerli bilgiler sunmuştur.',
        'img':'KASGARI.JPEG'
    },
    {
        'name':'Yusuf Has Hacib',
        'about':'"Mutluluk Veren Bilgi" anlamına gelen "Kutadgu Bilig" adlı eserini yazmıştır. Devlet yönetimi, adalet ve insan ilişkileri üzerine öğütler vermiştir. Türk-İslam edebiyatının ilk önemli eserlerinden biridir.',
        'img':'HACIB.JPG'
    },
    
]

# Create your views here.
def main(request):
    return render(
        request,
        'base.html',
        context={
            'peoples':[p['name'] for p in peoples]
        }
    )

def karakterler(request,index):
    p=peoples[index]
    
    return render(
        request,
        'people.html',
        context={
            'people':p
        }
    )