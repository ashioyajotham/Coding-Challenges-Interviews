name := "sql_evaluator"

version := "0.1"

scalaVersion := "2.13.3"

val circeVersion = "0.12.3"
libraryDependencies ++= Seq(
  "io.circe" %% "circe-core",
  "io.circe" %% "circe-generic",
  "io.circe" %% "circe-jawn",
).map(_ % circeVersion)

libraryDependencies ++= Seq("io.spray" %% "spray-json" % "1.3.5")

val writeRuntimeClasspathFile = taskKey[Unit]("Write the runtime classpath to a file.")

commands += Command.command("build") { s =>
  "compile" ::
  "writeRuntimeClasspathFile" ::
  s
}

writeRuntimeClasspathFile := {
  val classpathEntries = (fullClasspath in Runtime).value.files.map(_.getPath)
  val targetFile = (target in Runtime).value / "runtime-classpath"
  IO.write(targetFile, classpathEntries.mkString(":"))
}