![image](https://user-images.githubusercontent.com/5137066/129651827-27d701d4-68c7-4858-8669-bf646a91748d.png)

# rox-auto-harvest
Ragnarok X Next Generation - Auto Harvest by OpenCV-Python

### Credit: Thanapat Maliphan
Facebook: www.facebook.com/thanatos1995

### วิธีการติดตั้ง
1. ติดตั้งโปรแกรม Tesseract เพื่อให้โปรแกรมใช้สำหรับอ่านโจทย์
2. ดาวน์โหลดที่ `https://github.com/UB-Mannheim/tesseract/wiki`
3. ขั้นตอนการติดตั้ง กด Next อย่างเดียว
4. ทำการเพิ่ม Environment Variable ที่ This PC คลิกขวาเลือก Properties -> Advanced system settings -> กดปุ่ม Environment Variables...
5. ช่อง System Variables กดที่แถว Path แล้วกดปุ่ม Edit
6. เพิ่ม `C:\Program Files\Tesseract-OCR` และ `C:\Program Files\Tesseract-OCR\tessdata`
7. กด OK ทั้งหมด เพื่อทะยอยปิดหน้าต่าง
### วิธีใช้งาน
1. เปิดโปรแกรมบอท `rox_auto_harvest.exe`
2. เลือก Emulator ที่ใช้
3. กรอกจำนวนที่ต้องการ Limit เพื่อจำกัดจำนวนการเก็บเกี่ยว
4. กรอกจำนวนที่ต้องการ Cooldown เพื่อตั้งระยะเวลาห่างต่อครั้ง
5. เปิด Android Emulator เต็มจอ หรือ พยายามทำให้จอเกมมีขนาดใหญ่เพื่อการตรวจสอบคำถามกันบอทที่แม่นยำขึ้น
6. กด Enter เพื่อเข้าสู่สถานะ Harvesting โปรแกรมจะเริ่มทำงานทันที
7. หากต้องการปิดโปรแกรมกด `4`

### คำแนะนำ และ ข้อควรระวังในการใช้งาน
- รองรับ Windows เท่านั้น

### การใช้คีย์ลัด
- กด 1 เพื่อตั้งค่า Limit ใหม่
- กด 2 เพื่อตั้งค่า Cooldown ใหม่
- กด 3 เพื่อสลับสถานะเก็บเกี่ยว
- กด 4 เพื่อปิดโปรแกรม
