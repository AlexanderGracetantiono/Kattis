using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace false_security
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] code = {".-","-...","-.-.","-..",".","..-.","--.","...."
            ,"..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
            "-","..-","...-",".--","-..-","-.--","--..","..--",".-.-","---.","----"};
            string[] codealpha = {"A","B","C","D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U","V","W","X","Y","Z","_",",",".","?"};
            string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.?";
            string[] kalimat_data=new string[3000];
            //int zulutmp = 0;
           
            // for(int n = 0; n < 30; n++)
            //{
            //     Console.WriteLine(codealpha[n] + " = " + code[n]);
            // }
            int xx2x = 0;
            string input="ss";
            for (xx2x = 0; true; xx2x++)
            {
                input = Console.ReadLine();
                if (input == "" || input == null){ break; }
                kalimat_data[xx2x] = input;
            }
            for (int temp_xx = 0; temp_xx <=xx2x; temp_xx++)
            {
                if (kalimat_data[temp_xx]==null || kalimat_data[temp_xx] == "") { break; }
                int ztemp = 0;
                string wordouttemp = "";
                string kalimatcode = "", kalimatcodepanjang = "";
                for (int n = 0; n < kalimat_data[temp_xx].Length; n++)
                {
                    int a;

                    for (a = 0; a < 30; a++)
                    {
                        if (kalimat_data[temp_xx][n] == alphabet[a]) { break; }
                    }
                    kalimatcode = kalimatcode + code[a];
                    kalimatcodepanjang = kalimatcodepanjang + code[a].Length + "#";
                }
                string[] panjngcideurai = kalimatcodepanjang.Split('#');
                // Console.WriteLine(kalimatcode);
                int zulutempa = 0;
                for (int n = panjngcideurai.Length - 2; n >= 0; n--)
                {
                   
                    string tempcode = "";
                    //Console.Write(kalimatcodepanjang[n]);
                    //zulutmp += kalimatcodepanjang[n];
                    for (int m = int.Parse(panjngcideurai[n]); m > zulutempa; m--)
                    {

                        // Console.Write(m+"  ");
                        tempcode += kalimatcode[ztemp];
                        //Console.WriteLine(ztemp);
                        ztemp++;

                    }
                    //  zulutempa += kalimatcodepanjang[n];
                    for (int b = 0; b < 30; b++)
                    {
                        if (tempcode == code[b]) { wordouttemp += codealpha[b]; }


                    }

                }

                // Console.WriteLine(kalimatcodepanjang + " " + kalimatcode);
                Console.WriteLine(wordouttemp);
            }//endfor
            Console.ReadKey();


        }
    }
}
