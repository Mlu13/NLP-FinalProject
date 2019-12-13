import java.io.{BufferedWriter, File, FileWriter}
import scala.io.Source
import scala.collection.mutable.ListBuffer

object Clean extends App {

  val files = new File("/Users/Maggie/Documents/NlpProject/pymetamap-master/pymetamap/newcase/txtcopy").listFiles.map(_.getAbsolutePath).toList

  val newlist = files.drop(1)
//  val namelist = filesname.drop(1)

  var contentlist = new ListBuffer[String]()

    for(w <- 0 until newlist.length){


      try{
        val criteria = Source.fromFile(newlist(w).toString).getLines.mkString
        val regexinclu = "Record date:(.*)</TEXT>".r
        //
        val matches = regexinclu.findAllIn(criteria)

//        println("===Content===")

        val result = matches.group(1)
        //    println(criteria)
        //    println(matches)
//        println(result)

        val path = "/Users/Maggie/Documents/NlpProject/pymetamap-master/pymetamap/newcase/trimtxt/" + w.toString + ".txt"
        val file = new File(path)
        val bw = new BufferedWriter(new FileWriter(file))
        bw.write(result)
        bw.close()
        contentlist += result + "\n" * 2
      }
      catch{
        case exception: Exception => println("exception catch" + newlist(w).toString)
      }

    }

}
