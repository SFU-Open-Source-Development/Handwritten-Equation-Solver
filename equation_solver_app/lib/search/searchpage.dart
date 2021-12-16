import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:dio/dio.dart';
import 'package:http_parser/http_parser.dart';
class SearchPage extends StatelessWidget {
  const SearchPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
      alignment: Alignment.center,
      child: SearchClick(),
    ));
  }
}

class SearchClick extends StatefulWidget {
  const SearchClick({Key? key}) : super(key: key);

  @override
  State<SearchClick> createState() => _SearchClickState();
}

class _SearchClickState extends State<SearchClick> {
  late ImagePicker _picker;
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _picker = ImagePicker();
  }

  var _image;
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        imagePlaceholder(),
        SizedBox(height: 10),
        selectImage(),
        SizedBox(height: 10),
        sendImage(),
      ],
    );
  }

  Container imagePlaceholder() {
    return Container(
        alignment: Alignment.center,
        width: 300,
        height: 300,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: Colors.black,
            width: 1,
          ),
        ),
        child: _image == null ? 
        const Text('No image selected.') :
         Container(
           decoration: BoxDecoration(
             image: DecorationImage(
               image: FileImage(File(_image!.path)),
               fit: BoxFit.cover,
             ),
             borderRadius: BorderRadius.circular(20),
           ),
         ),
      );
  }

  Widget selectImage() {
    return InkWell(
        onTap: () async {
          var image = await _picker.pickImage(source: ImageSource.gallery);
          setState(() {_image = image;});
          // debugPrint(image!.path);
        },
        child: Container(
          width: 200,
          height: 80,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: Colors.blueAccent,
            borderRadius: BorderRadius.circular(20),
          ),
          child: const Text("Select Image",
              style: TextStyle(
                color: Colors.white,
              )),
        ));
  }
  Widget sendImage() {
    return InkWell(
        onTap: () async {
          var formData = FormData.fromMap({
            'file': await MultipartFile.fromFile(_image.path, filename: 'photo.jpg', contentType: MediaType('image', 'png')),
          });
          var response = await Dio().post('http://10.0.2.2:8000/upload', data: formData);
          debugPrint(response.data.toString());
        },
        child: Container(
          width: 200,
          height: 80,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: Colors.orange,
            borderRadius: BorderRadius.circular(20),
          ),
          child: const Text("Get Result",
              style: TextStyle(
                color: Colors.white,
              )),
        ));
  }
}
