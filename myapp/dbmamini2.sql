\c vehicle_renting

INSERT into Office values('KA001', 'RentIT-Hebbal', 'Hebbal');
INSERT into Office values('KA002', 'RentIT-Jayanagar', 'Jayanagar');
INSERT into Office values('KA003', 'RentIT-Bannerghatta', 'Bannerghatta');
INSERT into Office values('KA004', 'RentIT-JPNagar', 'JPNagar');
INSERT into Office values('KA005', 'RentIT-Koramangala', 'Koramangala');
INSERT into Office values('KA006', 'RentIT-Banashankari', 'Banashankari');
INSERT into Office values('KA007', 'RentIT-HSR', 'HSR');
INSERT into Office values('KA008', 'RentIT-Bellandur', 'Bellandur');

INSERT into Employee values('HE001', 'KA001', 'Ram', 'Singh', '1987-12-31', '#4, 5th cross, Hebbal', '9876543212');
INSERT into Employee values('HE002', 'KA001', 'Gopal', 'Rajput', '1985-01-31', '#5, 7th cross, Hebbal', '9856543212');
INSERT into Employee values('JY001', 'KA002', 'Srinivas', 'S', '1989-03-04', '#2, 2nd cross, 3rd block Jayanagar', '9856843212');
INSERT into Employee values('JY002', 'KA002', 'Manish', 'Venkat', '1988-06-22', '#9, 12th main, 6th block, Jayanagar', '9956543212');
INSERT into Employee values('BG001', 'KA003', 'Sita', 'Singhania', '1979-01-23', 'A-123, Eleganza, Bannerghatta main Road', '9996540000');
INSERT into Employee values('JP001', 'KA004', 'Gayathri', 'P', '1977-11-12', '#21, 7th phase, JP Nagar', '7856543212');
INSERT into Employee values('KR001', 'KA005', 'Selena', 'Malhotra', '1990-01-01', '#32, 7th main, Koramangala', '7746543212');
INSERT into Employee values('BS001', 'KA006', 'Vijaya', 'Kumar', '1988-03-27', '#5, 3rd stage, Banashankari', '6202345678');
INSERT into Employee values('HS001', 'KA007', 'Angie', 'Gomez', '1989-01-03', '#5, 7th main, 6th cross, HSR', '7658543212');
INSERT into Employee values('BL001', 'KA008', 'Pradeep', 'R', '1984-03-22', 'A-12, Sobha Carnival, Bellandur', '8856543212');

INSERT into Customer values('CU001','BL001', 'Aarav', 'Singh', '1987-02-30', 'A-2, Sobha Primrose, Bellandur', 'aarav12@gmail.com', '9872345671', NULL)
INSERT into Customer values('CU002', 'JY001', 'Mishika', 'Rao', '1985-08-08', 'Jayanagar 4th block', 'Mishika.Rao@gmail.com', '9002345671', NULL)
INSERT into Customer values('CU003', 'JY002', 'Aarya', 'Sinha', '1977-04-23', 'Jayanagar 5th block', 'aarya_23@gmail.com', '9842325671', 'KA-1320120123456')
INSERT into Customer values('CU004', 'JP001', 'Preesha', 'S', '1999-03-28', '#87/23 2nd main, JP Nagar 4th phase', 'Preesha1990@gmail.com', '8872300671', 'KA-1322120123356')
INSERT into Customer values('CU005', 'HS001', 'Keshav', 'Pandya', '1989-12-04', ' #5, 7th main, 6th cross, HSR', 'keshavp@gmail.com', '9822345671', 'KA-1234512345123')
INSERT into Customer values('CU006', 'JY001', 'Rachana', 'Sagar', '2000-09-19', '#224 Royal comforts Apartment, Jayanagar 4th block', 'rsagar34@gmail.com', '9872345244', NULL)
INSERT into Customer values('CU007', 'BL001', 'Kritika', 'Patel', '1990-04-22', 'B-4, Keerti Apartments, Bellandur', 'keertipatel@gmail.com', '9872345671', NULL)
INSERT into Customer values('CU008', 'KR001', 'Vivan', 'Singh', '1994-04-23', '80 Feet Road 4th Block, Koramangala', 'vivan1994@gmail.com', '9872345671', NULL)

INSERT into Driver values('DR093' ,NULL,  'BL001', 'Suresh', 'Singh', '1989-09-30', '#2, 9th cross, Bellandur', '9872345671',  NULL,  'KA 7984513578945');
INSERT into Driver values('DR099' , 'CU001',  'JY001', 'Ahaan', 'Khan', '1980-09-19', 'Madhavan park, Jayanagar 1st block', '9822000671',  '1555.24',  'KA 7224513578945');
INSERT into Driver values('DR045' , NULL,  'JP001', 'Suresh', 'Raina', '1985-06-22', '#2, 3rd phase, JP Nagar', '9885345671',  NULL,  'MH 8384513578945');
INSERT into Driver values('DR013' , 'CU003',  'BL001', 'Kabir', 'S', '1983-11-23', '#212, 5th cross, Bellandur', '9833445671',  '2553.24',  'RJ 6798513578945');
INSERT into Driver values('DR023' , 'CU008',  'JP001', 'Ramesh', 'H', '1985-03-24', '#99/43, 9th cross, 7th phase JP Nagar', '9834445671',  '1278.24',  'TN 4598451357894');
INSERT into Driver values('DR022' , NULL,  'KR001', 'Sudheer', 'P', '1993-05-12', '#256, 6th main, Koramangala', '9800945670',  NULL,  'KA 87933513511945');
INSERT into Driver values('DR094' , NULL,  'JY002', 'Jay', 'Singhania', '1993-11-23', ' 9th main, 4th T block Jayanagar', '8872344671',  NULL,  'KA 33944511577944');
INSERT into Driver values('DR033' , 'CU004',  'HS001', 'Sakshi', 'Sinha', '1983-07-17', '#2, 9th cross, 4th main HSR', '9872345671',  '1577.24',  'DL87984513578945');


INSERT into V_Owner values('OW213' , 'HE001',  'Naresh', 'L', '1980-11-03', '#248, 5th cross, Yeshwantpur', 'nareshL@gmail.com', '9791547515',  '2401.24');
INSERT into V_Owner values('OW313' , 'KR001',  'Leela', 'K', '1989-12-23', '8th cross, Koramangala', 'LeelaK@gmail.com', '9771547511',  '5000.30');
INSERT into V_Owner values('OW203' , 'HS001',  'Aayush', 'Kumar', '1989-09-24', '#24/56, 7th cross, 4th main, HSR', 'Akumar@gmail.com', '7791547515',  '2400.00');
INSERT into V_Owner values('OW100' , 'JY002',  'Sudharshan', 'P', '1989-12-04', '#72, 2nd cross, 6th block,  Jayanagar', 'SudarshanP@gmail.com', '9793546515',  '2503.00');
INSERT into V_Owner values('OW333' , 'JP001',  'Kartik', 'K', '1990-01-03', '#3, 5th phase, JP Nagar', 'Karthik@gmail.com', '9791667515',  '2101.00');
INSERT into V_Owner values('OW200' , 'BS001',  'Prateek', 'Srinivas', '1983-11-03', '#5, BSK 3rd stage', 'prateeks@gmail.com', '9791547515',  '2401.24');
INSERT into V_Owner values('OW123' , 'BG001',  'Satwik', 'P', '1977-04-13', 'A-1202, Esteem Enclave, Bannerghatta', 'SatwikP@gmail.com', '9793546315',  '2423.00');
INSERT into V_Owner values('OW345' , 'HS001',  'Advik', 'R', '1992-03-14', '#22/45, 5th main, 7th cross, HSR', 'AdvikR@gmail.com', '9891547716',  '2700.00');


INSERT into Office_PhNo values('KA001' , '08024579863');
INSERT into Office_PhNo values('KA001' , '08024579822');
INSERT into Office_PhNo values('KA002' , '08025579862');
INSERT into Office_PhNo values('KA002' , '08024579833');
INSERT into Office_PhNo values('KA003' , '08026579865');
INSERT into Office_PhNo values('KA004' , '08027579866');
INSERT into Office_PhNo values('KA005' , '08028579867');
INSERT into Office_PhNo values('KA006' , '08029579868');
INSERT into Office_PhNo values('KA006' , '08044579868');
INSERT into Office_PhNo values('KA007' , '08021579869');
INSERT into Office_PhNo values('KA008' , '08023579860');

INSERT into Payment values('PY121' , 'CU002',  'Card',  '2020-12-22', 1200.00, 250.00);
INSERT into Payment values('PY122' , 'CU004',  'Cash',  '2021-01-09', 1450.00, 270.00);
INSERT into Payment values('PY123' , 'CU005',  'UPI',  '2021-01-11', 2700.00, 230.00);
INSERT into Payment values('PY124' , 'CU006',  'NEFT',  '2021-01-29', 2120.00, 225.00);
INSERT into Payment values('PY125' , 'CU001',  'Card',  '2021-02-13', 1212.00, 100.00);
INSERT into Payment values('PY126' , 'CU002',  'UPI',  '2021-02-22', 2140.00, 150.00);
INSERT into Payment values('PY127' , 'CU003',  'Card',  '2021-03-25', 1300.00, 50.00);
INSERT into Payment values('PY108' , 'CU003',  'UPI',  '2021-05-03', 5560.00, 350.00);
