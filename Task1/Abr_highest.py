import sabre

class Abr_highest(sabre.Abr):
    def get_quality_delay(self, segment_index):
        manifest = self.session.manifest
        bitrates = manifest.bitrates
        throughput = self.session.get_throughput()
        buffers = self.session.get_buffer_contents()
        quality = len(bitrates) - 1
        return (quality, 0)