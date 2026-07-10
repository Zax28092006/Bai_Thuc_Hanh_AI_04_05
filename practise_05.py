Note = """
Bài tập 1
Ghi lại số giờ tự học (x) và điểm kiểm tra (y, thang điểm 10) của 5 sv như sau:
x(giờ)   1 2 3 4 5
--------------------------------
y(điểm)  2 4 5 4 6
Hãy tìm đường hồi quy y mũ = w_0 + w_1 * x theo phương pháp bình phương tối thiểu, rồi
đoán điểm của sinh viên học 6h
1) Hồi quy tuyến tính là gì?

Ta có 5 điểm dữ liệu (x, y). Nhìn vào dữ liệu thì ta thấy xu hướng:
học càng nhiều giờ, điểm càng cao.

Hồi quy tuyến tính đi tìm một đường thẳng "đi xuyên giữa" đám điểm để mô tả xu hướng đó.

y_hat = w_0 + w_1 * x

Trong đó:
+ w_0 là hệ số chặn (intercept): giá trị y_hat khi x = 0 (điểm nền).
+ w_1 là độ dốc (slope): mỗi khi x tăng lên 1 giờ, thì điểm dự đoán sẽ tăng thêm w_1.

Phần dư (residual) của mỗi điểm là khoảng cách dọc từ điểm thật đến đường e_i = y_i - y_hat_i
Một đường tối là 1 đường làm cho các phần dư nhỏ nhất

Phương pháp bình phương tối thiểu: chọn w_0, w_1 sap cho tổng bình phương phần dư là nhỏ nhất
SSE(w_0,w_1) = sum_i = 1 -> n (y_i - y_hat_i)^2 -> to min

Lấy đạo hàm SSE theo w_0 và w_1 rồi cho bằng 0 (đạo hàm của công thức chuỗi), ta được công thức:
w_1 = sum[(x_1 - x_)(y_i - y_)] / sum(x_i - x_)^2 = S_xy / S_xx
w_0 = y_daoHam - w_1 * x_
Trong đó:
(x_, Y_) là điểm trung bình.

Nhận xét:
w_1 = "x và y cùng biến thiên bao nhiêu" / "x trải rộng bao nhiêu"
Công thức w_0 cho thấy đường hồi quy luôn đi qua điểm trung bình (x_, y_).
        """
Note = """
Bài tập 1
Ghi lại số giờ tự học (x) và điểm kiểm tra (y, thang điểm 10) của 5 sv như sau:
x(giờ)   1 2 3 4 5
--------------------------------
y(điểm)  2 4 5 4 6
Hãy tìm đường hồi quy y mũ = w_0 + w_1 * x theo phương pháp bình phương tối thiểu, rồi
đoán điểm của sinh viên học 6h
1) Hồi quy tuyến tính là gì?

Ta có 5 điểm dữ liệu (x, y). Nhìn vào dữ liệu thì ta thấy xu hướng:
học càng nhiều giờ, điểm càng cao.

Hồi quy tuyến tính đi tìm một đường thẳng "đi xuyên giữa" đám điểm để mô tả xu hướng đó.

y_hat = w_0 + w_1 * x

Trong đó:
+ w_0 là hệ số chặn (intercept): giá trị y_hat khi x = 0 (điểm nền).
+ w_1 là độ dốc (slope): mỗi khi x tăng lên 1 giờ, thì điểm dự đoán sẽ tăng thêm w_1.

Phần dư (residual) của mỗi điểm là khoảng cách dọc từ điểm thật đến đường e_i = y_i - y_hat_i
Một đường tối là 1 đường làm cho các phần dư nhỏ nhất

Phương pháp bình phương tối thiểu: chọn w_0, w_1 sap cho tổng bình phương phần dư là nhỏ nhất
SSE(w_0,w_1) = sum_i = 1 -> n (y_i - y_hat_i)^2 -> to min

Lấy đạo hàm SSE theo w_0 và w_1 rồi cho bằng 0 (đạo hàm của công thức chuỗi), ta được công thức:
w_1 = sum[(x_1 - x_)(y_i - y_)] / sum(x_i - x_)^2 = S_xy / S_xx
w_0 = y_daoHam - w_1 * x_
Trong đó:
(x_, Y_) là điểm trung bình.

Nhận xét:
w_1 = "x và y cùng biến thiên bao nhiêu" / "x trải rộng bao nhiêu"
Công thức w_0 cho thấy đường hồi quy luôn đi qua điểm trung bình (x_, y_).
        """