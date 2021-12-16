import 'dart:async';

import 'package:equation_solver/search/searchpage.dart';
import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({ Key? key }) : super(key: key);

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  late Timer timer;
  @override
  void initState() {
    super.initState();
    timer = Timer.periodic(const Duration(seconds: 3), (timer) {
      Navigator.of(context).pushReplacement(
        MaterialPageRoute(builder:(context) => SearchPage()));
    });}
  @override
  void dispose() {
    // TODO: implement dispose
    super.dispose();
    timer.cancel();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Row(
          children: [
            SizedBox(width: 20),
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const <Widget>[
                Text("SFU", style: TextStyle(color: Colors.redAccent, fontSize: 36, fontWeight: FontWeight.bold),),
                Text("Development Club", style: TextStyle(color: Colors.redAccent, fontSize: 24, fontWeight: FontWeight.bold),),
                Text("Equation Solver", style: TextStyle(color: Colors.black38, fontSize: 24, fontWeight: FontWeight.bold),),
              ],
            ),
          ],
        )
      ),
    );
  }
}