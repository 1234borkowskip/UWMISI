using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cw4
{
    class Student : Osoba
    {
        public int rok;
        public int numerGrupy;
        public int numerAlbumu;

        public Student(string imie, string nazwisko, int dataUrodzenia, string miejsceZamieszkania, int rok, int numerGrupy, int numerAlbumu) : base(imie, nazwisko, dataUrodzenia, miejsceZamieszkania)
        {
            this.rok = rok;
            this.numerGrupy = numerGrupy;
            this.numerAlbumu = numerAlbumu;
        }

        public void Wypiszinfo()
        {
            Console.WriteLine(imie + " " + nazwisko + " " + dataUrodzenia + " " + miejsceZamieszkania + " " + rok + " " + numerGrupy + " " + numerAlbumu);
        }
    }
}
