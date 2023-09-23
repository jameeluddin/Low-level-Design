from Design_patterns.CompositeDesignPattern.Solution1WithCompositeDesign.directory import Directory
from Design_patterns.CompositeDesignPattern.Solution1WithCompositeDesign.file import File


def main():
    movie_directory = Directory("Movie")
    border = File("Border")
    movie_directory.add(border)

    comedy_movie_directory = Directory("Comedy_Movie")

    hulhcul = File("Hulchul")
    comedy_movie_directory.add(hulhcul)
    movie_directory.add(comedy_movie_directory)
    movie_directory.ls()


if __name__ == "__main__":
    main()
