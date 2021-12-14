import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class SearchPage extends StatelessWidget {
  const SearchPage({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
       alignment: Alignment.center, 
       child: SearchClick(),
      )
    );
  }
}

class SearchClick extends StatefulWidget {
  const SearchClick({ Key? key }) : super(key: key);

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
  var image;
  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () async {
        image = await _picker.pickImage(source: ImageSource.gallery);
      },
      child: Container(
        width: 200,
        height: 100,
        color: Colors.blue,
        alignment: Alignment.center,
        child: Text("Select Image")
      )
    );
  }
}