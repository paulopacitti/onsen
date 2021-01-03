use std::fs::File;
use std::io;
use rodio::Sink;

fn main() -> Result<(), io::Error> {
   let (_stream, stream_handle) = rodio::OutputStream::try_default().unwrap();
   let sink = Sink::try_new(&stream_handle).unwrap();

   // Load a sound from a file, using a path relative to Cargo.toml
   let file = File::open("assets/rain.wav").unwrap();
   let source = rodio::Decoder::new_looped(io::BufReader::new(file)).unwrap();
   sink.append(source);

   // The sound plays in a separate audio thread,
   // so we need to keep the main thread alive while it's playing.
   // Press ctrl + C to stop the process once you're done.
  loop {}
}
