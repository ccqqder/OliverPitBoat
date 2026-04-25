---
title: "Kana Juku Dev Log (Phần 1): Từ Chatbots đến AI Agent"
date: 2026-02-22T13:16:34.278Z
author: "QQder"
categories:
  - Hội thảo
tags:
  - Ứng dụng iOS
  - AI trên thiết bị
  - Nhận dạng chữ viết tay
  - udemy
  - Claude
  - mã Claude
  - song tử
  - song tử cli
  - swiftUI
  - UIKit
keywords:
  - đặc vụ AI
  - mã Claude
  - song tử cli
  - phát triển iOS
  - nhà phát triển độc lập
  - kana juku
  - học tiếng nhật
  - swiftUI
  - AI trên thiết bị
  - tác phẩm
  - chatbot
description: "Chia sẻ kinh nghiệm phát triển ứng dụng đầu tiên của tôi, Kana Juku - hành trình cũng đánh dấu sự chuyển đổi của tôi từ chatbot sang tác nhân AI"
---


# Lời nói đầu

Kana Juku là ứng dụng đầu tiên tôi xây dựng và đưa lên App Store.

Vì đây là lần đầu tiên của tôi nên có cả một câu chuyện đầy đủ để chia sẻ.

Loạt bài này bao gồm quá trình phát triển, cách tôi sử dụng hỗ trợ AI và cách nó phát triển, làm việc với các tập dữ liệu công cộng và cân nhắc về bản quyền, v.v.

Nếu các ứng dụng khác có những câu chuyện đáng chú ý, tôi sẽ xuất bản riêng những câu chuyện đó.

Bài đăng này tập trung vào quá trình chuyển đổi từ chatbot sang tác nhân AI bắt đầu từ **Q4 năm 2025**.

Mọi thứ diễn ra rất nhanh trong không gian này nên tôi đã thẳng thắn đánh dấu thời gian cho những khoảnh khắc quan trọng.

## Giới thiệu về ứng dụng

Nếu bạn có thiết bị Apple, vui lòng tải xuống và dùng thử.

Một số bài đăng sắp tới cũng sẽ sử dụng ứng dụng này làm ví dụ đang chạy — các chủ đề như dọn dẹp [bộ dữ liệu ETL](https://etlcdb.db.aist.go.jp/), [Apple Create ML](https://developer.apple.com/machine-learning/create-ml/), [PyTorch](https://pytorch.org/), [VOICEVOX](https://voicevox.hiroshiba.jp/), mô hình ngôn ngữ lớn trên thiết bị, v.v.

Kana Juku: [URL](https://apps.apple.com/us/app/%E5%81%87%E5%90%8D%E7%A7%81%E5%A1%BE/id6756785942)

![](/images/IMG_2433.JPG)

***

# Dòng thời gian phát triển

### Động lực

Tôi và gia đình đều thích học tiếng Nhật và từ lâu tôi đã mong muốn có một ứng dụng học tiếng Nhật hoàn toàn phù hợp với nhu cầu của mình.

Điểm đau đầu của gia đình tôi là họ không đọc được tiếng Anh nên chữ romaji trong hầu hết sách giáo khoa và ứng dụng đều vô nghĩa đối với họ.

Đối với tôi, tôi thực sự muốn kana được hiển thị cùng với nguồn gốc chữ kanji của chúng (ví dụ: "あ" bắt nguồn từ "安").

Một điều khó chịu khác: Tôi đã cài đặt bàn phím tiếng Nhật để thỉnh thoảng sử dụng, nhưng việc chuyển đổi phương thức nhập hàng ngày đồng nghĩa với việc phải nhấn thêm một lần nữa để bỏ qua bàn phím tiếng Nhật - một chút xích mích đã tăng thêm.

### Chuẩn bị sớm

**[Quý 4 năm 2024]**

Vào thời điểm đó, tôi đang nghỉ việc nên tôi có đủ thời gian để tham gia các khóa học [Udemy](https://www.udemy.com/). Vì tôi đã có một số kinh nghiệm về JavaScript nên tôi bắt đầu với [React](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwih6Kzo2O-SAxUl3zQHHZoSL-kQFnoECDYQAQ&url=https%3A%2F%2Fzh-hant.legacy.reactjs.org%2F&usg=AOvVaw3Q6fqYyboB_gQOnPVX_tbN&opi=89978449) & [Expo](https://expo.dev/).

Ở giai đoạn này, tôi đang theo dõi nội dung khóa học - các trang kiểu web đơn giản cùng với các tính năng bổ sung như GPS, điều khiển máy ảnh và tìm nạp dữ liệu từ xa.

Nhưng vì đây không phải là hệ sinh thái gốc của Apple nên có rất nhiều công cụ bổ sung cần quản lý.

**[Quý 1 năm 2025]**

Sau một thời gian đắn đo, tôi đã mua một chiếc Mac Mini và chuyển hoàn toàn sang SwiftUI của chính Apple. Một lần nữa, tôi đã học được từ các khóa học của Udemy.

Phần lớn thời gian của tôi dành cho việc làm quen với các thành phần và bố cục giao diện người dùng cơ bản, cùng với tất cả các tính năng cơ bản - lưu giữ dữ liệu, tìm nạp dữ liệu, nhúng bản đồ - và các tính năng tương đương SwiftUI của chúng.

SwiftUI hiện đại hơn và không được kết hợp chặt chẽ với Xcode như UIKit, nhưng cũng khó dự đoán bố cục SwiftUI thực sự sẽ trông như thế nào. Ngay từ đầu, tôi đã quan tâm quá nhiều đến điều đó và đã dành rất nhiều thời gian để thử nghiệm.

**[Quý 3 năm 2025]**

Vì tôi có một công việc ban ngày và chỉ có thể viết mã vào buổi tối - chứ không phải mỗi buổi tối - nên tiến độ rất chậm. Về cơ bản, tôi đang xây dựng bộ khung cơ bản và cắm dữ liệu tiếng Nhật vào.

Với ứng dụng đầu tiên, thật khó để đoán trước hình dạng cuối cùng nên tôi liên tục chỉnh sửa. Đôi khi tôi quay lại để xem lại các video khóa học để biết các tính năng mà giờ đây tôi biết mình cần. Về cơ bản, tôi đã trả học phí.

Tính đến thời điểm này, bắt đầu từ **Q1 2024**, các chatbot đơn giản như ChatGPT đã trợ giúp rất nhiều cho việc viết mã.

Nhưng chu trình sao chép-dán và phải giải thích hàng núi ngữ cảnh tốn rất nhiều thời gian. Kết quả đầu ra thường không đạt yêu cầu trong lần thử đầu tiên hoặc bị sai hướng, khiến tôi phải quay lại vòng lặp sao chép-dán. Nó chưa bao giờ đạt đến chu kỳ phản hồi tích cực — nó chỉ hữu ích như một tài liệu tham khảo học tập.

Vào thời điểm đó, công cụ phổ biến nhất thực sự là trình chỉnh sửa Con trỏ với tính năng tự động hoàn thành tab, nhưng nó yêu cầu đăng ký để sử dụng có ý nghĩa, vì vậy tôi **không thử**.

Trong khi đó, Claude đã trở nên nổi tiếng với tư cách là mô hình viết mã tốt nhất và Anthropic đã phát hành Claude Code - một tác nhân AI chạy trên máy cục bộ của bạn. Nhưng một lần nữa, nó yêu cầu đăng ký nên tôi đã không thử.

***

### Chuyển hướng sang các tác nhân AI

**[Quý 4 năm 2025]**

Tại thời điểm này, tôi dự kiến ​​mình chỉ đăng ký một chatbot mỗi lần và tôi vừa chuyển từ ChatGPT sang Google Gemini.

Phát triển theo hướng đặc tả (SDD) đang là xu hướng và Google đã tung ra Gemini CLI — câu trả lời của họ cho Claude Code — vì vậy cuối cùng tôi **đã thử**.

Tôi phát hiện ra rằng các đại lý đã loại bỏ hoàn toàn bước sao chép-dán, giúp nâng cao hiệu quả một cách đáng kể. Bước dán lại mã và tìm xem dòng nào cần thay đổi cũng không còn nữa.

Lúc đó tôi đã bị thuyết phục: để viết mã, bạn nên sử dụng một tác nhân chứ không phải chatbot. Vì vậy, tôi đã tiếp tục và đăng ký Claude để sử dụng Mã Claude (CC kể từ đây trở đi).

Mô hình cơ bản của CC rõ ràng mạnh hơn. Khả năng hiểu các cuộc hội thoại và khả năng thực hiện như mong đợi của nó vốn đã rất đáng tin cậy.

#### Điều khiển máy tính và Opus 4.5

Một lần, đĩa Mac Mini của tôi đã đầy và máy không thể sử dụng được. Tôi vừa hỏi CC phải làm gì — giống như cách tôi đặt câu hỏi trên trang web của chatbot.

CC đã quay lại với một kế hoạch cụ thể: những thư mục nào có thể bị xóa, những gì có thể được chuyển sang ổ đĩa ngoài, v.v.

Tôi lo lắng nó có thể làm hỏng máy tính của tôi nên tôi chấp thuận từng bước một. Cuối cùng, mọi thứ đều diễn ra suôn sẻ.

Tôi không quen lắm với macOS hoặc môi trường xây dựng Xcode. Đó là khi tôi nhận ra rằng AI có ít nhất 80% hiểu biết về *mọi thứ* — kể cả những điều tôi không biết — và khả năng viết mã gần tương đương với khả năng vận hành máy tính.

Vì CC có thể trực tiếp điều khiển máy nên nó di chuyển tự do giữa các thư mục, viết mã, nhìn thấy lỗi của chính mình và sửa chúng - một vòng phản hồi tích cực hoàn toàn tự duy trì.

Tốc độ phát triển với một đại lý ở một cấp độ hoàn toàn khác, và việc tôi phải đợi thêm ba tháng trước khi chuyển sang CC khiến tôi cảm thấy khá ngu ngốc.

Thời gian lãng phí thật đáng kinh ngạc, cả về mặt chủ quan và khách quan.

Về mặt chủ quan: nếu tôi áp dụng các công cụ mới nhất sớm hơn thì ba tháng làm việc trước đó có thể hoàn thành trong hai đến ba tuần.

Khách quan mà nói: những người khác sử dụng các công cụ mới nhất làm việc hiệu quả hơn tôi và vận chuyển sản phẩm của họ sớm hơn.

Việc tôi từ chối thử trước đây - có thể tiết kiệm nửa giờ thời gian thiết lập và vài trăm đô la phí đăng ký - cuối cùng đã lãng phí rất nhiều thời gian trong cuộc đời tôi.

Điều này cũng có thể giải thích tại sao rất nhiều người bị ám ảnh bởi việc theo đuổi những tin tức mới nhất về sản phẩm AI.

Ít nhất đó là cách đối với tôi - tôi không thể không cập nhật các bản phát hành mới nhất. Đó là một hình thức phòng ngừa rủi ro quản lý thời gian.

**[Ngày 24 tháng 11 năm 2025]**

Opus 4.5 đã được phát hành. Opus là mẫu hàng đầu cao cấp nhất của Claude và phiên bản 4.5 vừa bị loại bỏ.

Ngoài những cải tiến đáng kể về hiệu suất so với người tiền nhiệm, điểm khác biệt lớn nhất là sự hiểu biết về ý định.

Phiên bản cũ về cơ bản đã thực hiện chính xác những gì bạn đã chỉ ra (thành thật mà nói thì nó đã khá tốt rồi). Bắt đầu từ phiên bản 4.5, sau khi nhận được yêu cầu của bạn, trước tiên nó sẽ tóm tắt và lập kế hoạch ở một mức độ nào đó. Về mặt con người: nó trở nên sắc bén hơn, giàu kinh nghiệm hơn.

Bạn không còn cần phải chỉ ra tập tin nào cần sửa đổi và cách sửa đổi. Bạn có thể mô tả mục tiêu cuối cùng giống như một người quản lý hoặc người điều hành, và nó sẽ chia nhỏ mục tiêu đó ra và tự lên kế hoạch cho một số bước tiếp theo.

Khả năng lập kế hoạch này thậm chí còn nâng cao hiệu quả hơn nữa. Như tôi đã đề cập, AI đã biết ít nhất 80% mọi thứ - giờ đây nó đang chủ động thực hiện các bước công việc tiếp theo và thực hiện tốt chúng.

Kết hợp với điều này, tôi có thể vận hành ở mức độ trừu tượng cao hơn nhiều. Ngày càng có nhiều người được giao phó cho CC. Dần dần, tôi không còn cần phải tự đọc hoặc chỉnh sửa mã nữa.

Sau khi Opus 4.5 ra mắt, cuộc tranh luận trên mạng xã hội về việc liệu AI có thể viết mã về cơ bản đã kết thúc hay không.

Đối với các kỹ sư phần mềm toàn thời gian và các chuyên gia dày dạn kinh nghiệm, tôi không thể nói về kinh nghiệm của họ.

Nhưng so với bản thân tôi: những việc mà lẽ ra tôi phải mất một đến hai năm thì giờ đây có thể hoàn thành trong hai đến ba tháng.

Kết quả đầu ra nằm ngoài phạm vi hiểu biết của tôi - tôi thực sự là nút thắt lớn nhất.

*Hết Phần 1*
