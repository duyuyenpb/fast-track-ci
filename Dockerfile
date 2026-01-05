# Dùng Python nhỏ gọn nhất
FROM python:3.9-slim

# Tạo thư mục làm việc trong container
WORKDIR /app

# Cài thư viện pytest
RUN pip install pytest

# Copy toàn bộ code ở vào container
COPY . .

# Lệnh mặc định khi container chạy: Chạy pytest
CMD ["pytest", "-v"]