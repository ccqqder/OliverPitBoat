---
title: "Hành tinh Gantt: Vị trí thích hợp và những điều cần cân nhắc của nhà phát triển độc lập"
date: 2026-02-25T06:55:21.349Z
draft: false
categories:
  - Đài thiên văn
tags:
  - Nhà phát triển độc lập
  - Cửa hàng ứng dụng
  - Biểu đồ Gantt
  - Phát triển sản phẩm
  - Phát triển được hỗ trợ bởi AI
  - dự án phụ
keywords:
  - nhà phát triển độc lập
  - Cửa hàng ứng dụng
  - biểu đồ Gantt
  - Hành tinh Gantt
  - phát triển sản phẩm
  - dự án phụ
  - Phát triển được hỗ trợ bởi AI
  - biểu đồ Gantt cuộc sống
  - Trực quan hóa 3D
  - Ứng dụng iOS
description: "App Store là trang chủ cá nhân thời đại mới, sử dụng Gantt Planet làm nghiên cứu điển hình"
author: "QQder"
---


![](/images/gantt-planet-cover.jpg)

# Lời nói đầu

Trong bài đăng này, tôi sẽ nói về thị trường, tài nguyên, hệ sinh thái và quá trình phát triển dưới góc nhìn của một nhà phát triển độc lập.
Là một trình cắm không biết xấu hổ, tôi đang sử dụng Gantt Planet làm ví dụ đang chạy của mình: [URL](https://apps.apple.com/us/app/%E7%94%98%E7%89%B9%E6%98%9F%E7%90%83/id6757654373).
Tôi sẽ thừa nhận trước rằng đây chỉ là những dự án phụ của tôi - áp lực rất khác so với những người kiếm sống từ việc này - vì vậy tôi chỉ thảo luận về phương pháp nghiên cứu ở đây.

## Tia lửa và gian hàng

Ý tưởng đằng sau Gantt Planet rất đơn giản: các công cụ biểu đồ Gantt miễn phí — cho dù là phần mềm máy tính để bàn, ứng dụng di động hay ứng dụng web — đều khá tệ khi sử dụng.
Những ứng dụng thực sự có vẻ hợp lý đều tính phí, vì vậy tôi nghĩ mình sẽ xây dựng ứng dụng biểu đồ Gantt của riêng mình.

Không mất nhiều thời gian trước khi tôi nhận ra mọi chuyện không đơn giản như vậy:

1. Xem biểu đồ Gantt kiểu bảng tính trên màn hình điện thoại quá chật chội
2. Biểu đồ Gantt phù hợp cần kết nối với nhiều tài nguyên - email, địa chỉ liên hệ, phòng họp, v.v.

Giải quyết một trong những vấn đề này là tốn kém. Bạn sẽ cần phải dành rất nhiều thời gian để tinh chỉnh giao diện người dùng và thiết kế các luồng sử dụng lý tưởng, đồng thời chấp nhận rằng một số quy trình công việc không thể tích hợp được và phải loại bỏ.

Đối với việc tích hợp tài nguyên, bạn cần xử lý các hoạt động đăng nhập cho tất cả các nền tảng chính, xử lý vô số API và giao thức xác thực, đồng thời duy trì tất cả những hoạt động đó trong tương lai.

Tại thời điểm này, tôi đã gặp phải một bức tường - và khi bạn đang làm việc ở quy mô không được hưởng lợi từ tính kinh tế nhờ quy mô, điều đó là không thể tránh khỏi.

## Xoay vòng sau xoay vòng

Trong những khoảnh khắc như thế này, tôi muốn tận dụng từng yếu tố và mở rộng nó ra bên ngoài một hoặc hai bước, tìm kiếm một giao điểm khả thi nơi mọi thứ có thể thực sự hoạt động.

Là một nhà phát triển được thúc đẩy bởi lợi ích cá nhân, "khả thi" có nghĩa là chi phí cực thấp, cộng với một đề xuất giá trị tuy nhỏ nhưng được xác định rõ ràng.

AI đã giúp tôi đạt được phần đầu tiên – chi phí cực thấp.

Về phần giá trị, nó chủ yếu do người dùng tự xác định, mặc dù việc đưa ra các ý tưởng từ AI cũng có thể giúp kết tinh mọi thứ.

Đối với tôi, vấn đề chủ yếu là xây dựng thứ gì đó mà tôi thực sự muốn sử dụng - ít nhất là thứ mà tôi thích nhìn vào. Ngoài ra, nếu chưa có ai khác làm điều đó thì không có phiên bản miễn phí hoặc có sự khác biệt rõ ràng, điều đó cũng được tính là giá trị.

Tại thời điểm này, tôi bắt đầu tự hỏi: có cái gì giống biểu đồ Gantt nhưng thực sự không phải là biểu đồ Gantt không?

Và rồi một hình ảnh hình thành trong tâm trí tôi.

Tôi nhớ rằng khi sử dụng biểu đồ Gantt, tôi có xu hướng đặt những mục quan trọng hơn xuống dưới.

Mục dưới cùng thường là điều kiện tổng thể để hoàn thành toàn bộ dự án - hoặc nó thể hiện chính dự án đó.

Nhưng điều gì sẽ xảy ra nếu có những món đồ thậm chí còn ở dưới hàng dưới cùng đó - những món đồ thậm chí còn quan trọng hơn? Đó sẽ là gì?

Chà, có rất nhiều thứ quan trọng hơn - chúng không liên quan gì đến công việc. Họ nói về tôi. Về cuộc sống.

Và thế là nó quyết định: Tôi sẽ không xây dựng biểu đồ Gantt cho doanh nghiệp thông thường. Tôi định xây dựng **biểu đồ Gantt cuộc sống**.

![](/images/gantt-planet-chart-en.png)

## Bước tiếp theo

Vì vậy, tôi quyết định xây dựng biểu đồ Gantt phù hợp với trường hợp sử dụng kinh doanh thông thường.

Điều này thuận tiện có nghĩa là tôi không còn cần phải tích hợp với các dịch vụ trực tuyến nữa,

bởi vì bây giờ tất cả là về người dùng - chỉ họ, và không có gì khác.

Với điều đó, tôi đã tiến thêm một bước nữa và duy trì dự án cho đến thời điểm hiện tại. Nhưng liệu nó có thể dẫn đến đủ chất để hoàn thiện không?

Tôi nghĩ về khả năng tự quản lý và những điều quan trọng nhưng không cấp bách trong cuộc sống - tất cả đều có nhịp điệu và tần số.

Vấn đề sức khỏe là vấn đề nên các công ty phải kiểm tra sức khỏe hàng năm. Gia đình rất quan trọng nên bạn hãy nhớ gặp lại những người thân yêu của mình trước khi thời gian trôi qua quá lâu.

Kết hợp với tính chất của biểu đồ Gantt, trong bất kỳ khoảng thời gian nhất định nào, các mục sẽ trùng lặp với ngày hiện tại.

Và nếu bạn xem xét khoảng thời gian của cả cuộc đời, mọi món đồ đều có khả năng phù hợp với ngày hôm nay. Điều đó có nghĩa là tôi có thể thu gọn mọi thứ vào đường trung tâm của giao diện người dùng.

Điều này đã giải quyết vấn đề giao diện người dùng chật chội trong khi thể hiện một tập hợp các giá trị mà tôi thấy thực sự có ý nghĩa.

![Chế độ xem chính của dòng thời gian](/images/screenshots/gantt-planet/timeline-en.png)
*Chế độ xem dòng thời gian thực tế: tất cả các mục trong cuộc sống đều hội tụ trên đường trung tâm của lịch - xem nhanh mọi thứ quan trọng hôm nay*

## Tính đầy đủ

Một trong những nguyên tắc đánh giá của App Store là ứng dụng của bạn không thể sao chép những gì một trang web văn bản thuần túy có thể làm được.

Ví dụ: một danh sách việc cần làm đơn giản có thể không đạt yêu cầu. Vì vậy, tôi phải đảm bảo rằng ứng dụng này không chỉ là một bảng tính — nếu không, Google Trang tính cũng có thể làm được điều tương tự.

Luồng hình ảnh từ trên xuống dưới của bảng tính khiến tôi nhớ đến việc đào sâu xuống - giống như mỗi ngày bạn chỉ thực hiện các nhiệm vụ ở mức độ bề mặt tối thiểu. Có một thành ngữ Trung Quốc, “mọi người lơ lửng trên công việc của mình”, thể hiện trạng thái này một cách hoàn hảo.

Phép ẩn dụ về những món đồ quan trọng hơn nằm ở các lớp sâu hơn khiến tôi muốn làm cho nó trở nên trực quan hơn, hữu hình hơn. Mối liên hệ trước mắt là việc khai quật - đào qua các tầng địa chất, khai thác mỏ.

Sau đó đến vấn đề thực hiện. Tôi có nên uốn cong từng hàng của bảng tính một chút không? Thêm một số biến dạng phối cảnh?

Tôi nghĩ về bối cảnh của biểu đồ Gantt cuộc sống này - đơn độc và nội tâm.

Hình ảnh hiện lên trong đầu tôi là: trên bề mặt lớp vỏ của một hành tinh, một người đang đào một mình. Và rồi tôi chợt nhận ra - đó không phải là cậu bé tóc vàng tưới hoa hồng và thuần hóa một con cáo sao?

Vì vậy, tôi đã xây dựng phiên bản 3D của biểu đồ Gantt, sử dụng trục mỏ và đá quý làm hình ảnh thể hiện các hạng mục việc cần làm.

Một cách tiếp cận triệt để hơn nữa có lẽ là chỉ giữ lại phiên bản hành tinh, nhưng xem xét khả năng sử dụng, độ khó khi xem xét và mức độ hiểu trực quan của nó, tôi quyết định giữ cả hai quan điểm.

![](/images/gantt-planet-3d-en.png)

![Chế độ xem hành tinh 3D](/images/screenshots/gantt-planet/geo-view-en.png)
*Biểu đồ Gantt hành tinh 3D — hầm mỏ và đá quý là sự thể hiện trực quan cho các mục tiêu cuộc sống*

## Vẫn thiếu bàn làm việc

Hồi còn đi học, tôi đã dành rất nhiều thời gian ngồi yên ở bàn làm việc một mình - học hoặc viết.

Sử dụng và suy nghĩ về cuộc sống này, biểu đồ Gantt như đưa tôi trở lại chiếc bàn đó - chiếc bàn đã bị vứt đi từ lâu.

Nếu tôi hoàn thành một việc gì đó, tôi chỉ làm ba tháng một lần hoặc mỗi năm một lần - hoặc thậm chí là một mục tiêu dài hạn -

Tôi nghĩ tôi thực sự muốn viết nhật ký, hoặc có thể viết một lá thư cho một người bạn thân.

Tôi nhận ra biểu đồ Gantt này vẫn còn thiếu một lối thoát cảm xúc cuối cùng. Nhưng nếu tôi thêm tính năng chia sẻ trên mạng xã hội, người dùng sẽ không thể hoàn toàn trung thực.

Một tùy chọn khác là nhắn tin trong ứng dụng giữa những người dùng, nhưng sẽ không bao giờ - hiện tại hoặc trong tương lai - có đủ lượt cài đặt để hỗ trợ điều đó hoặc ít nhất cũng cần phải có phiên bản Android. Dù sao đi nữa, nó không cần thiết đối với phiên bản đầu tiên.

Giải pháp phù hợp nhất mà tôi nghĩ đến là giải pháp linh hoạt nhất: chatbot.

Cung cấp cho chatbot một loạt tác phẩm văn học kinh điển và để nó đóng vai trò là một "cái rỗng trên cây" - một người bạn tâm giao - cung cấp cho người dùng một số phản hồi chu đáo.

## suy nghĩ cuối cùng

Đó là quá trình phát triển sản phẩm và ra quyết định đằng sau ứng dụng này.

Có vẻ như tôi cứ liên tục thay đổi hướng đi cho đến khi hoàn thành, nhưng trên thực tế, có rất nhiều ý tưởng bị loại bỏ và các tính năng bị từ chối mà tôi thậm chí còn chưa đề cập đến.

Ngoài việc cung cấp cho những người bạn tò mò một cái nhìn sâu hơn về các loại cân nhắc trong quá trình phát triển sản phẩm,

điều cuối cùng tôi muốn nhấn mạnh — và câu trả lời cho tiêu đề — là thị trường ngách và sự cân nhắc của nhà phát triển độc lập là: **làm bất cứ điều gì khiến bạn hạnh phúc!**

Tôi chắc chắn nhiều người sẽ cho rằng điều này quá phù hợp hoặc không phù hợp với sở thích hoặc giá trị của họ.

Nhưng dù vậy, với một chút thời gian và sự trợ giúp của AI, bạn có thể xây dựng thứ bạn muốn nhưng vẫn chưa tồn tại.

Bạn trở thành ông chủ - quyết định điều gì có giá trị và điều gì đáng xây dựng.

Bạn trở thành nhà thiết kế - chọn bố cục, màu sắc, phông chữ và hình ảnh yêu thích của bạn.

Bạn sẽ trở thành Thủ tướng - quyết định cách viết nó và mức độ hoàn thiện của các tính năng.

AI sẽ chỉ mạnh hơn. Ngay cả khi nó không thể làm được mọi thứ ngày hôm nay thì trong tương lai gần, bạn cũng sẽ có thể tận hưởng tất cả những điều này.

App Store hiện là trang chủ cá nhân thời đại mới — mọi người đều có thể xuất bản câu chuyện của riêng mình.

Nếu bạn quan tâm, hãy theo dõi blog này. Tôi sẽ tiếp tục chia sẻ những trải nghiệm và suy ngẫm thực tế khi xuất bản trên App Store.
