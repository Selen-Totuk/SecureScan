# SecureScan - Web Güvenlik Tarayıcı

**SecureScan**, web güvenliği alanındaki bilgimi ve becerilerimi sergileyen bir projedir. Bu uygulama, bir web sitesinin güvenliğini taramak için geliştirilmiştir. Web uygulamalarının güvenliğini sağlamanın, günümüz yazılım geliştirme sürecinde ne kadar kritik olduğunun farkındalığıyla bu projeyi hayata geçirdim. Projem, özellikle SSL sertifikası ve HTTPS yönlendirme kontrolleri ile web güvenliği testlerini hızlandırmayı amaçlamaktadır.

Bu projeyi, yazılım geliştirme, güvenlik ve web uygulamaları üzerine öğrendiğim becerileri derinleştirerek ve problem çözme yeteneklerimi geliştirmek için yaptım. Bu, portföyümde yer alan projelerden sadece bir tanesidir ve özellikle güvenlik odaklı çalışmalara olan ilgimi göstermektedir.

## Teknolojiler

- **Python**: Projenin backend tarafında Python dilini kullandım. Flask web framework'u ile RESTful API geliştirdim.
- **Flask**: Python tabanlı web framework'u, uygulamanın hızlıca geliştirilmesi ve çalıştırılması için kullanıldı.
- **Requests**: Web sitesine yapılan HTTP isteklerini yönetmek için kullanıldı.
- **Flask-CORS**: Farklı domainlerdeki istekleri işlemek için kullanılan CORS desteği.
- **HTML/CSS/JavaScript**: Kullanıcı arayüzünü oluşturmak için basit frontend teknolojileri kullanıldı.

## Proje Özellikleri

- **SSL Sertifikası Kontrolü**: Web sitesinin SSL sertifikasının geçerli olup olmadığını kontrol eder.
- **HTTPS Yönlendirme Kontrolü**: Web sitesinin HTTPS'ye yönlendirip yönlendirmediğini test eder.
- **Kullanıcı Dostu Arayüz**: Web tarayıcı tabanlı arayüz ile kullanıcıların URL girerek güvenlik taraması yapmasını sağlar.
- **Gelişmiş Güvenlik Testi**: Web güvenliği konusunda yapılan testler, daha kapsamlı uygulamalar için temel sağlar.

## Kullanım

Bu proje, web güvenliği konusunda farkındalık yaratmak ve basit bir güvenlik tarayıcısı oluşturmak için geliştirilmiştir. Uygulamanın kullanımı oldukça basittir:

1. **Uygulamayı Çalıştırın**:
   - Python yüklü olduğundan emin olun.
   - Projenin bulunduğu dizine gidin ve `server.py` dosyasını çalıştırarak Flask sunucusunu başlatın:
     ```bash
     python server.py
     ```

2. **Tarayıcıda Uygulamayı Açın**:
   - Uygulama başladığında, tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

3. **URL Tarama**:
   - Web arayüzüne bir web sitesi adresi (örneğin, google.com) girin ve "Tara" butonuna tıklayın.
   - Uygulama, SSL sertifikasını ve HTTPS yönlendirmelerini denetleyecek ve güvenlik hakkında size rapor sunacaktır.

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. **Python ve Bağımlılıkları Yükleyin**:
   - Proje klasörüne gidin ve gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:
     ```bash
     pip install -r requirements.txt
     ```

2. **Uygulamayı Başlatın**:
   - `server.py` dosyasını çalıştırarak Flask uygulamasını başlatın:
     ```bash
     python server.py
     ```

## Katkıda Bulunma

Bu proje açık kaynaklıdır ve katkı sağlamak isteyen herkesin katkı sunmasını memnuniyetle karşılıyorum.

- Repo'yu forkladıktan sonra, kendi branch'ınızı oluşturun.
- Yapmak istediğiniz değişiklikleri commit edin.
- Pull request gönderin.

## Geliştirme Süreci ve Öğrendiklerim

- **Yazılım Güvenliği**: Bu projede, SSL sertifikalarının ve HTTPS yönlendirmelerinin güvenlik açısından ne kadar önemli olduğunu öğrendim. Web sitelerinin güvenliğini sağlamak için gerekli önlemleri almak, gerçek dünyada kritik bir beceridir.
- **Web Uygulama Geliştirme**: Flask kullanarak web uygulamaları geliştirme ve RESTful API oluşturma konusunda deneyim kazandım.
- **Problem Çözme ve Yaratıcılık**: Projenin her aşamasında karşılaştığım teknik engelleri çözerek yaratıcı çözümler ürettim.

## Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır.

