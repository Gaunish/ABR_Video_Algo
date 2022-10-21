import sabre

class Abr_Lowest(sabre.Abr):
    def get_quality_delay(self, segment_index):
        manifest = self.session.manifest
        bitrates = manifest.bitrates
        throughput = self.session.get_throughput()
        buffers = self.session.get_buffer_contents()
        quality = 0
        return (quality, 0)