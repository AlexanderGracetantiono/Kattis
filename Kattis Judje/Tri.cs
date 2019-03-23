using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tri
{
    class Program
    {
        static void Main(string[] args)
        {
            string masuk = Console.ReadLine();
            string[] cek = masuk.Split(' ');
            int[] data = new int[3];
            data[0] = int.Parse(cek[0]);
            data[1] = int.Parse(cek[1]);
            data[2] = int.Parse(cek[2]);

            if (data[0] + data[1] == data[2]) { Console.WriteLine(data[0] + "+" + data[1] + "=" + data[2]); }
            else if(data[0] == data[1] + data[2]) { Console.WriteLine(data[0] + "=" + data[1] + "+" + data[2]); }

            else if (data[0] - data[1] == data[2]) { Console.WriteLine(data[0] + "-" + data[1] + "=" + data[2]); }
            else if (data[0] == data[1] - data[2]) { Console.WriteLine(data[0] + "=" + data[1] + "-" + data[2]); }
            
            else if (data[0] / data[1] == data[2]) { Console.WriteLine(data[0] + "/" + data[1] + "=" + data[2]); }
            else if (data[0] == data[1] / data[2]) { Console.WriteLine(data[0] + "=" + data[1] + "/" + data[2]); }
            
            else if (data[0] * data[1] == data[2]) { Console.WriteLine(data[0] + "*" + data[1] + "=" + data[2]); }
            else if (data[0] == data[1] * data[2]) { Console.WriteLine(data[0] + "=" + data[1] + "*" + data[2]); }
            Console.ReadKey();
        }
    }
}
