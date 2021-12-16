import 'package:equation_solver/home/home.dart';
import 'package:equation_solver/search/searchpage.dart';
import 'package:equation_solver/style.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Home(),
      theme: defaultThemeData(),
    );
  }
}